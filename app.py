

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

@app.route('/favicon.ico')
def favicon():
    return 'no hay'

#@app.route('/API/iris', methods=['POST'])
#def ApiIris():
#    datos = []    
#    datos.append(float(request.form['sepal_length']))
#    datos.append(float(request.form['sepal_width']))
#    datos.append(float(request.form['petal_length']))
#    datos.append(float(request.form['petal_width']))

#    return jsonify(model.predict([datos])[0])



if __name__ == '__main__':
    app.run()
