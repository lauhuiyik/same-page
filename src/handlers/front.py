##########

import web
from lib.utils import render
from lib.etherpad import pad

##########

class FrontPage:

    def GET(self):
        content = pad.getHTML(padID = 'thisisguan')
        web.debug(content)
        return render('index.html')

    def POST(self):
        pass

