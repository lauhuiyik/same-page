##########

import web
import hmac
from hashlib import sha256

from lib.utils import db
from lib.utils import render
from lib.utils import etherpad

##########

class LoginPage:

    def GET(self):
        return render('login.html')

    def POST(self):
        uid = web.input().login_uid
        pw = web.input().login_pw

        # DB select based on username
        # Will raise exception if not valid
        try:
            login_user = db.select('users', where = 'username = $uid',
                                   vars = locals())[0]
        except:
            # TODO return error mesage using ajax
            return render('login.html')
        
        # This will be executed if try block is executed
        # This is because except block returns value
        
        # Each user has a different salt
        # SHA256 used because it's better than default MD5
        # Rehash password and check if equal to database's
        hashed_pw = hmac(login_user['salt'], pw, sha256)
        
        # Hashed password with user's salt matches!
        # Moves on to process the remember me toggle
        # Sets cookies accordingly
        # Redirects to /home
        if hashed_pw == user['pw']:

            # Exception checking using to-string conversion
            # Raises error if not remember me is not toggled
            try:
                # Remember me toggle is 'on'
                # 'on' as in string and literally on
                rmb_me = str(web.input().rmb_me)
                rmb_me = True

            # Oddly there is only 'on', no 'off'
            # So this will trigger an AttributeError (string)
            except AttributeError:
                rmb_me = False

            # Sets the cookie expiration to 3 months
            # Resets cookie expiration on every login
            if rmb_me:
                # make_cookie( uid, hashed_pw, salt )
                # cookie = uid|hashed_pw|salt
                web.setcookie('login_info',
                              make_cookie(uid, hashed_pw),
                              7776000)
                raise web.seeother('/home')

            # Session only login, remember me is False
            else:
                web.setcookie('login_info',
                              make_cookie(uid, hashed_pw))
                raise web.seeother('/home')

        # Input password does not match the one in database
        # Renders the html with notice
        else:
            # TODO do this rendering with Ajax request
            return render('login.html')



