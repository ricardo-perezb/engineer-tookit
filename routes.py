from flask import Flask, url_for
from flask import render_template
from flask.ext.bower import Bower

app = Flask(__name__, static_url_path='')
Bower(app)

@app.route('/')
def showRoot():
  return render_template('index.html')

@app.route('/calculators/<ctype>')
def showCalculator(ctype):
  return render_template('calculator_' + ctype + '.html')

