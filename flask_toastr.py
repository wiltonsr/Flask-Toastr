from jinja2 import Markup
from flask import current_app

class _toastr(object):
    @staticmethod
    def include_toastr_js(version='2.1.4', local_js=None):
        js = ''
            if local_js is not None:
                js = '<script src="%s"></script>\n' % local_js
            elif version is not None:
                js_filename = 'toastr.min.js'
                js = '<script src="//cdnjs.cloudflare.com/ajax/libs/' \
                     'toastr.js/%s/%s"></script>\n' % (version, js_filename)
        return Markup(js)

    @staticmethod
    def include_toastr_css(version='2.1.4', local_css=None):
        css = ''
            if local_css is not None:
                css = '<link href="%s" rel="stylesheet" />\n' % local_js
            elif version is not None:
                css_filename = 'toastr.min.css'
                css = '<link href="//cdnjs.cloudflare.com/ajax/libs/' \
                      'toastr.js/%s/%s" rel="stylesheet" />\n' % (version, css_filename)
        return Markup(css)

    @staticmethod
    def include_jquery(version='2.1.0', local_js=None):
        js = ''
        if local_js is not None:
            js = '<script src="%s"></script>\n' % local_js
        else:
            js = ('<script src="//code.jquery.com/' +
                  'jquery-%s.min.js"></script>') % version
        return Markup(js)

class Toastr(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['toastr'] = _toastr
        app.context_processor(self.context_processor)

    @staticmethod
    def context_processor():
        return {
            'toastr': current_app.extensions['toastr']
        }

    def create(self, timestamp=None):
        return current_app.extensions['toastr'](timestamp)
