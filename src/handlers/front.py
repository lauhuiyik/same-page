##########

import web
from lib.utils import render
from lib.utils import etherpad

##########

class FrontPage:

    def GET(self):
        return render('front.html')

    def POST(self):
        pass

