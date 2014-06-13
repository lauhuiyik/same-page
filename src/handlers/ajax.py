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
        data = memcache.get('data')

        self.response.headers['Content-Type'] = 'application/json'   
        obj = {
            'data': data, 
        } 
        self.response.out.write(json.dumps(obj))
        
    def post(self):
        data = self.request.get('doc')
        log.info('New data: '+ data)

        memcache.set('data', data)

