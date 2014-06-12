##############################################################################

import os
import webapp2
import logging
from google.appengine.ext import db
from google.appengine.api import memcache

from base_handler import BaseHandler

##############################################################################

class FrontPage(BaseHandler):

    def get(self):
        self.render('index.html')

    def post(self):
        pass

