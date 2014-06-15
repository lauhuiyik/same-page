##########

import re
import random

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
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range(16):
        chars.append(random.choice(ALPHABET))
    return "".join(chars)

