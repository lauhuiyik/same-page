##############################################################################

import os
import json
import webapp2

from handlers.front import FrontPage
from handlers.ajax import AjaxHandler

##############################################################################

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([
      ('/', FrontPage),
      ('/ajax', AjaxHandler),],
      config = config, debug = True)

if __name__ == '__main__':
    app.run()
    
