from flask import Flask, flash, render_template
from flask_toastr import Toastr

app = Flask(__name__)
toastr = Toastr(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def index():
    # Default Title
    flash("Info Category and Default Title")
    flash("Info Category and Default Title", 'info')
    flash("Success Category and Default Title", 'success')
    flash("Error Category and Default Title", 'error')
    flash("Warning Category and Default Title", 'warning')
    # Custom Title
    flash("Info Category", 'Custom Title')
    flash({'title': "Custom Title", 'message': "Info Category"},)
    flash({'title': "Custom Title", 'message': "Error Category"}, 'error')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
