##########

import web
import hmac
from time import strftime
from datetime import datetime
from hashlib import sha256

from lib.utils import db
from lib.utils import render
from lib.utils import etherpad
from lib.validate import valid_user, valid_pw, make_salt

##########

class FrontPage:

    def GET(self):
        return render('front.html')

    def POST(self):
        web.debug(web.input())
        uid = web.input().signup_uid
        pw = web.input().signup_pw
        
        if valid_user(uid) and valid_pw(pw):

            # Makes random 16-character alphabet
            # Stored in the db
            salt = make_salt()

            # Specifies that hmac uses sha256 instead of md5
            # hmac complicates the hash
            hashed_pw = hmac.new(salt, pw, sha256).hexdigest()

            db.insert('users', username = uid, 
                      pw = hashed_pw, salt = salt,
                      joined = datetime.now())

            raise web.seeother('/work')

        else:
            raise web.seeother('/')

