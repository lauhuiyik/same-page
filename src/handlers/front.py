##########

import web
from lib.jinja_handler import render

##########

class FrontPage:

    def GET(self):
        return render('index.html')

    def POST(self):
        pass

