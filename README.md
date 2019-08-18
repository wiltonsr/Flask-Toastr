Flask-Toastr
============

[![](https://img.shields.io/badge/python-3.4+-blue.svg)](https://www.python.org/download/releases/3.4.0/) [![](https://img.shields.io/badge/python-2.7+-blue.svg)](https://www.python.org/download/releases/2.7.2/) [![](https://img.shields.io/github/license/ResidentMario/missingno.svg)](https://github.com/wiltonsr/Flask-Toastr/blob/master/README.md)

Showing Flask's flash non-blocking notifications in templates using [toastr](https://github.com/CodeSeven/toastr).

Donate to help keep this project maintained.
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=5QJ62BNMRC75W&currency_code=USD&source=url">
<img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" /></a>

Quick Start
-----------

Step 1: Initialize the extension:

    from flask_toastr import Toastr
    toastr = Toastr(app)

Step 2: In your `<head>` and bottom of `<body>`sections of your base template add the following code:

```html
<html>
  <head>
    {{ toastr.include_jquery() }}
    {{ toastr.include_toastr_css() }}
    {{ toastr.message() }}
  </head>
  <body>
    {{ toastr.include_toastr_js() }}
  </body>
</html>
```

This extension also supports the [Flask application factory pattern](http://flask.pocoo.org/docs/latest/patterns/appfactories/) by allowing you to create a Toastr object and then separately initialize it for an app:

        toastr = Toastr()

        def create_app(config):
            app = Flask(__name__)
            app.config.from_object(config)
            # initialize toastr on the app within create_app()
            toastr.init_app(app)

        app = create_app(prod_config)

Note that jQuery is required. If you are already including it on your own then you can remove the `include_jquery()` line. Secure HTTP is used if the request under which these are executed is secure.

The `include_jquery()`, `include_toastr_js()` and `include_toastr_css()` methods take some optional arguments. If you pass a `version` argument to any of these calls, then the requested version will be loaded from the default CDN. In addition, it is also possible to pass `js_filename` and `css_filename` to `include_toastr_js()` and `include_toastr_css()`, respectively.

Step 3: Use the `flash()` method with or without category in your views. For example:

```python
@app.route('/')
def index():
    flash("All OK")
    flash("All OK", 'success')
    flash("All Normal", 'info')
    flash("Not So OK", 'error')
    flash("So So", 'warning')
    return render_template('index.html')
```

Step 4: Enjoy

Parameters
--------

Config                    | Default           | Possible Values         | Description
------------------------- | ----------------- | ----------------------- | -------------
TOASTR_VERSION            | '2.1.4'           | [Releases from here](https://github.com/CodeSeven/toastr/releases) | Version of Toastr
TOASTR_JQUERY_VERSION     | '2.1.0'           | [Releases from here](https://github.com/jquery/jquery/releases) | Version of JQuery
TOASTR_CSS_FILENAME       | 'toastr.min.css'  | CDN file name           | CSS Filename used in CDN Toastr's link
TOASTR_JS_FILENAME        | 'toastr.min.css'  | CDN file name           | JS Filename used in CDN Toastr's link
TOASTR_CLOSE_BUTTON       | 'true'            | 'true' or 'false'       | Enable or Disable close button
TOASTR_TIMEOUT            | 15000             | any `int` value (in ms) | Time to notification close
TOASTR_EXTENDED_TIMEOUT   | 1000              | any `int` value (in ms) | Time to notification close after hover mouse or click
TOASTR_POSITION_CLASS     | 'toast-top-right' | 'toast-top-right', 'toast-bottom-right', 'toast-bottom-left', 'toast-top-left', 'toast-top-full-width', 'toast-bottom-full-width', 'toast-top-center', 'toast-bottom-center' | Notification Positon
TOASTR_PREVENT_DUPLICATES | 'false'           | 'true' or 'false'       | Doesn't show same notification
TOASTR_NEWS_ON_TOP        | 'false'           | 'true' or 'false'       | Notification's aparition order
TOASTR_PROGRESS_BAR       | 'true'            | 'true' or 'false'       | Enable or Disable progress bar
TOASTR_OPACITY            | True              | True or False           | Enable or Disable notification's opacity

    Note: The values `true` and `false` are passed to JS, that is Case Sensitive.
    Therefore they must be passed in lowercase.

Examples
--------

```
To run the example in your local environment::

  1. Clone the repository::

        git clone https://github.com/wiltonsr/Flask-Toastr.git
        cd Flask-Toastr

  2. Create and activate a virtual environment::

        virtualenv env
        source env/bin/activate

  3. Install requirements::

        pip install -r 'example/requirements.txt'

  4. Run the application::

        python example/app.py
```

Function Reference
------------------

Consult the [toastr documentation](https://github.com/CodeSeven/toastr#toastr) for more details.

Development
-----------

This extension is just a project to improve my python and flask skills. Any suggestions or tips are welcome.
