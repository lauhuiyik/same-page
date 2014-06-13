##############################################################################

import os
import json
import logging as log

from google.appengine.ext import db
from google.appengine.api import memcache

from base_handler import BaseHandler

##############################################################################

class AjaxHandler(BaseHandler):
    
    def get(self):
        doc_name = self.request.cookies.get('doc') 
        doc_dir = os.path.join(os.path.dirname(__file__),
                               'tmp', doc_name)
        with open(doc_dir, 'r') as f:
            content = f.read()

        return content
        
    def post(self):
        data = self.request.get('doc')
        log.info('New data: '+ data)

        doc_name = self.request.cookies.get('doc')
        doc_dir = os.path.join(os.path.dirname(__file__),
                               'tmp', doc_name)
        
        f = open(doc_dir, 'w')
        f.write(data)
        f.close()

