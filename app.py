# app.py
"""Flask App Project."""

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index(name=None):
    return render_template('index.html', name=name)
@app.route('/l', methods=['GET'])
def lol():
    return "lol"

@app.route('/favicon.ico')
def favicon():
    return 'no hay'

if __name__ == '__main__':
    app.run()