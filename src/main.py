#!/usr/bin/env python
##########

import web
from handlers.front import FrontPage
from handlers.work import WorkPage

##########

urls = ('/work', 'WorkPage',
        '/', 'FrontPage')

app = web.application(urls, globals())

##########

if __name__ == "__main__":
    app.run()

