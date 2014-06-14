##########

import web
from lib.utils import render
from lib.utils import etherpad

##########

class WorkPage:

    def GET(self):
        content = etherpad.getHTML(padID = 'thisisguan')
        web.debug(content)
        return render('index.html')

    def POST(self):
        pass

