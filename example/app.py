from flask import Flask, render_template
from flask_toastr import Toastr

app = Flask(__name__)
toastr = Toastr(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
