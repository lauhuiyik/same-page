# For jinja2 template loader.
# Always check the os.path.dirname, if there's a bug in template loading.
#

import os
from jinja2 import Environment,FileSystemLoader

def render(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')),
            extensions=extensions,
            )
    jinja_env.globals.update(globals)
    return jinja_env.get_template(template_name).render(context)
