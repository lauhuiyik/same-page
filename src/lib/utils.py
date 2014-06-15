##########

import os
import web
import pylibmc
from etherpad_lite import EtherpadLiteClient
from jinja2 import Environment,FileSystemLoader

##########

def render(template_name, **context):
    """
    Jinja2 Template Handler
    This function renders the html template Jinja2 style
    Extra parameters for substituting into html
    """

    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(loader = FileSystemLoader(
                            os.path.join(os.path.dirname(
                            os.path.dirname(__file__) ), 'templates') ),
                            extensions=extensions)
    jinja_env.globals.update(globals)
    return jinja_env.get_template(template_name).render(context)

##########

"""
Initialize Memcache

binary = True
This specifies that client talks to memcached servers using the binary protocol.

'tcp_nodelay' =  True
Setting this behavior will enable the TCP_NODELAY socket option which makes sense for TCP connections.

'ketama' = True
Setting this behavior is a shortcut for setting 'hash' to 'md5' and distribution to 'consistent ketama'.
"""
memcache = pylibmc.Client(['127.0.0.1'], binary = True,
                          behaviors = {
                              'ketama': True,
                              'tcp_nodelay': True,
                          })
                          

##########

"""
Initializes etherpad instance
"""
etherpad = EtherpadLiteClient(base_params = {
        'apikey': '2cf9c48c15aa877c1aad4383aa2bd6abf7de75986f6ba036f90ba9ef18ac274c'
    })


"""
Configuration for db
"""
db = web.database(user = 'guanhao97',
                  dbn = 'postgres',
                  db = 'same_page',
                  pw = '55popo')


