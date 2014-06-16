##########

import web

from lib.utils import render, etherpad, memcache
from lib.validate import valid_login

##########

class HomePage:

    def GET(self):
        
        # Checks if db's password matches cookie's
        if valid_login():
            return render('index.html')

        # User does not have access to content
        # Or user has been changing cookie values
        else:
            raise web.seeother('/')

    def POST(self):
        pass

