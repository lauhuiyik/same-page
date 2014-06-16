##########

import web
from lib.utils import render
from lib.utils import etherpad

##########

class HomePage:

    def GET(self):
        return render('index.html')

    def POST(self):
        pass

