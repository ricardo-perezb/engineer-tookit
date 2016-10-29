from flask import Flask, url_for
from flask import render_template
from flask.ext.bower import Bower

app = Flask(__name__, static_url_path='')
Bower(app)

@app.route('/')
def showRoot():
  return render_template('index.html')

@app.route('/calculator/rpn')
def rpnCalculator():
  return 'RPN calculator - under construction'

