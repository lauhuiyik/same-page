##############################################################################

import os
import json
import webapp2

from handlers.front import FrontPage

##############################################################################

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([
      ('/', FrontPage),
      ('/login', LoginPage)],
      config = config, debug = True)

if __name__ == '__main__':
    app.run()
    
