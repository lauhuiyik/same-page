#!/usr/bin/env python
##########

import web
from handlers.front import FrontPage
from handlers.home import HomePage

##########

urls = ('/home', 'HomePage',
        '/', 'FrontPage')

app = web.application(urls, globals())

##########

if __name__ == "__main__":
    app.run()

