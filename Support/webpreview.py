
# python bindings for soryu's web-preview
from os import environ, path
from tm_helpers import sh, sh_escape

webpreview = sh_escape(path.join(environ["TM_SUPPORT_PATH"], "lib/webpreview.sh"))

def html_header(title, subtitle):
    return sh('source %s; html_header "%s" "%s"' % (webpreview, title, subtitle))

def html_footer():
    return sh('source %s; html_footer' % webpreview)


