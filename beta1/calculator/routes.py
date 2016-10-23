from flask import Flask, url_for
from flask import render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def showRoot():
    return url_for('static', filename='index.html')

@app.route('/calculator/rpn')
def rpnCalculator():
    return 'RPN calculator - under construction'

