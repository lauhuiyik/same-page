##############################################################################

from google.appengine.ext import db
from google.appengine.api import memcache

from base_handler import BaseHandler

##############################################################################

class FrontPage(BaseHandler):

    def get(self):
        self.render('index.html')
        self.response.set_cookie('doc', 'guanhao')

    def post(self):
        pass

