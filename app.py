#pip install Flask

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from sklearn.externals import joblib

import pandas as pd
#from matplotlib import pyplot as plt
import matplotlib
import numpy as np

import scipy
import imutils
#from scipy.spatial import distance as dist
#from imutils import perspective
#from imutils import contours
import argparse
import imutils
import cv2

#   from settings import PROJECT_ROOT
import os

app = Flask(__name__)

#PEOPLE_FOLDER = os.path.join('static', 'people_photo')
#app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

# model = joblib.load('decisiontreeiris.pkl')

# app.config["CACHE_TYPE"] = "null"
# some time later
#cache.init_app(app)

@app.route('/', methods=['GET'])
def index(name=None):
    return render_template('index.html', name=name)
@app.route('/l', methods=['GET'])
def lol():
	return "lol"

#@app.route('/API/iris', methods=['POST'])
#def ApiIris():
#    datos = []    
#    datos.append(float(request.form['sepal_length']))
#    datos.append(float(request.form['sepal_width']))
#    datos.append(float(request.form['petal_length']))
#    datos.append(float(request.form['petal_width']))

#    return jsonify(model.predict([datos])[0])



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
