#!/usr/bin/env python
##########

import web
from handlers.front import FrontPage

##########

urls = ('/', 'FrontPage')

app = web.application(urls, globals())
db = web.database(user = 'guanhao97',
                  dbn = 'postgres',
                  db = 'site_db',
                  pw = '')

##########

if __name__ == "__main__":
    app.run()

