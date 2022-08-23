# -*- coding: utf-8 -*-
try:
    from jinja2 import Markup
except ImportError:
    from markupsafe import Markup
from jinja2 import Template
from flask import current_app, render_template, get_flashed_messages


class _toastr(object):
    @staticmethod
    def include_toastr_js(version=None, js_filename=None):
        if version is None:
            version = current_app.config.get('TOASTR_VERSION')
        if js_filename is None:
            js_filename = current_app.config.get('TOASTR_JS_FILENAME')
        js = '<script src="//cdnjs.cloudflare.com/ajax/libs/' \
             'toastr.js/{0}/{1}"></script>\n'.format(version, js_filename)
        return Markup(js)

    @staticmethod
    def include_toastr_css(version=None, css_filename=None):
        if version is None:
            version = current_app.config.get('TOASTR_VERSION')
        if css_filename is None:
            css_filename = current_app.config.get('TOASTR_CSS_FILENAME')
        css = '<link href="//cdnjs.cloudflare.com/ajax/libs/' \
              'toastr.js/{0}/{1}" rel="stylesheet" />\n'.format(
                version,
                css_filename
                )
        if current_app.config.get('TOASTR_OPACITY'):
            return Markup(css)
        else:
            return Markup('''
<style type = text/css>
  #toast-container>div {{
    opacity: 1 !important;
  }}
</style> {0}'''.format(css))

    @staticmethod
    def include_jquery(version=None):
        if version is None:
            version = current_app.config.get('TOASTR_JQUERY_VERSION')
        js = ('<script src="//code.jquery.com/' +
              'jquery-{0}.min.js"></script>'.format(version))
        return Markup(js)

    @staticmethod
    def message():
        toastr_options = 'toastr.options.closeButton = %s; \
        toastr.options.showEasing = \"%s\"; \
        toastr.options.hideEasing = \"%s\"; \
        toastr.options.closeEasing = \"%s\"; \
        toastr.options.showMethod = \"%s\"; \
        toastr.options.hideMethod = \"%s\"; \
        toastr.options.closeMethod = \"%s\"; \
        toastr.options.timeOut = %s; \
        toastr.options.extendedTimeOut = %s; \
        toastr.options.positionClass = \"%s\"; \
        toastr.options.preventDuplicates = %s; \
        toastr.options.newestOnTop = %s; \
        toastr.options.progressBar = %s; ' % (
            current_app.config.get('TOASTR_CLOSE_BUTTON'),
            current_app.config.get('TOASTR_SHOW_EASING'),
            current_app.config.get('TOASTR_HIDE_EASING'),
            current_app.config.get('TOASTR_CLOSE_EASING'),
            current_app.config.get('TOASTR_SHOW_METHOD'),
            current_app.config.get('TOASTR_HIDE_METHOD'),
            current_app.config.get('TOASTR_CLOSE_METHOD'),
            current_app.config.get('TOASTR_TIMEOUT'),
            current_app.config.get('TOASTR_EXTENDED_TIMEOUT'),
            current_app.config.get('TOASTR_POSITION_CLASS'),
            current_app.config.get('TOASTR_PREVENT_DUPLICATES'),
            current_app.config.get('TOASTR_NEWS_ON_TOP'),
            current_app.config.get('TOASTR_PROGRESS_BAR'))
        message = Template('''
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <script type="text/javascript">
      (function($) {
        $(document).ready(function() {
          {{ toastr_options }}
          {% for category, message in messages %}
            {% if category is undefined or category == 'message' %}
              {% set category = 'info' %}
            {% endif %}
            {% if message is mapping %}
              toastr.{{ category }}(\'{{ message['message'] | replace("'","\\\\'") }}\', \'{{ message['title'] | replace("'","\\\\'") }}\')
            {% elif category not in ['message', 'error', 'warning', 'info', 'success'] %}
              toastr.info(\'{{ message | replace("'","\\\\'") }}\', \'{{ category|capitalize }}\')
            {% else %}
              toastr.{{ category }}(\'{{ message | replace("'","\\\\'") }}\', \'{{ category|capitalize }}\')
            {% endif %}
          {% endfor %}
        });
      })(jQuery);
    </script>
  {% endif %}
{% endwith %}
''')
        return Markup(render_template(
          message,
          get_flashed_messages=get_flashed_messages,
          toastr_options=toastr_options)
          )


class Toastr(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['toastr'] = _toastr
        app.context_processor(self.context_processor)

        app.config.setdefault('TOASTR_VERSION', '2.1.4')
        app.config.setdefault('TOASTR_JQUERY_VERSION', '2.1.0')
        app.config.setdefault('TOASTR_CSS_FILENAME', 'toastr.min.css')
        app.config.setdefault('TOASTR_JS_FILENAME', 'toastr.min.js')

        app.config.setdefault('TOASTR_CLOSE_BUTTON', 'true')
        app.config.setdefault('TOASTR_SHOW_EASING', 'swing')
        app.config.setdefault('TOASTR_HIDE_EASING', 'linear')
        app.config.setdefault('TOASTR_CLOSE_EASING', 'linear')
        app.config.setdefault('TOASTR_SHOW_METHOD', 'fadeIn')
        app.config.setdefault('TOASTR_HIDE_METHOD', 'fadeOut')
        app.config.setdefault('TOASTR_CLOSE_METHOD', 'fadeOut')
        app.config.setdefault('TOASTR_TIMEOUT', 15000)
        app.config.setdefault('TOASTR_EXTENDED_TIMEOUT', 1000)
        app.config.setdefault('TOASTR_POSITION_CLASS', 'toast-top-right')
        app.config.setdefault('TOASTR_PREVENT_DUPLICATES', 'false')
        app.config.setdefault('TOASTR_NEWS_ON_TOP', 'false')
        app.config.setdefault('TOASTR_PROGRESS_BAR', 'true')
        app.config.setdefault('TOASTR_OPACITY', True)

    @staticmethod
    def context_processor():
        return {'toastr': current_app.extensions['toastr']}

    def create(self, timestamp=None):
        return current_app.extensions['toastr'](timestamp)
