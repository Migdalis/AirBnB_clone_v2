#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """ display C followed by the value of the text """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text='is cool'):
    """ display Python, followed by the value of the text """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ display “n is a number” only if n is an integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ display a HTML page only if n is an integer """
    if n % 2 == 0:
        t = 'even'
    else:
        t = 'odd'
    return render_template('6-number_odd_or_even.html', num=n, e_o=t)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')