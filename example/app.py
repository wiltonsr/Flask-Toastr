from flask import Flask, flash, render_template
from flask_toastr import Toastr

app = Flask(__name__)
toastr = Toastr(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def index():
    flash("All OK")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
