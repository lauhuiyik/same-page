##########

import re
import web
import hmac
import random
from hashlib import sha256

from lib.utils import db, memcache

##########

"""
validate module for validating usernames, passwords and emails for Sign Up feature.
"""

def valid_user(user):
	USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
	if len(user)>=6:
		return USER_RE.match(user)

def valid_pw(pw):
	PW_RE = re.compile("^.{3,20}$")
	if len(pw)>=6:
		return PW_RE.match(pw)

def valid_email(email):
	EMAIL_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")
	if len(email)>=6:
		return EMAIL_RE.match(email)

def make_salt():
    """
    Generates 16-character salt for encrypting passwords.
    Encryption done with SHA256 via HMAC.
    """
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range(16):
        chars.append(random.choice(ALPHABET))
    return "".join(chars)

def make_cookie(uid, pw, salt):
    cookie = uid + '|' + pw + '|' + salt
    return cookie

def valid_login():
    login_cookie  = web.cookies().get('login_info')

    # login_cookie in the form of 'username|hashed_pw'
    # Splitted login_cookie = ['username', 'hashed_pw']
    login_cookie = login_cookie.split('|')
    uid = login_cookie[0]
    pw = login_cookie[1]

    # Checks if memcache has password
    db_pw = memcache.get(uid + '_login')

    # Does DB Query when not available
    # Sets uid_login to password
    if db_pw is None:
        user = db.select('users', where = 'username = $uid',
                         vars = locals())[0]
        db_pw = user['pw']
        memcache.set(uid + '_login', db_pw)

    # Checks if they are the same
    # Renders html
    if pw == db_pw:
        return True

    # Redirects to front page
    else:
        return False



