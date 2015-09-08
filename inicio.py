from flask import Flask  
from flask import render_template

app = Flask(__name__)

@app.route('/')
def inicio():
	return render_template('inicio.html')

@app.route('/MSD')
def msd():
	return render_template('msd.html')

@app.route('/RDF')
def rdf():
	return render_template('rdf.html')

@app.route('/dislocaciones')
def dislocaciones():
	return render_template('dislocaciones.html')

@app.route('/estructuras')
def estructuras():
	return render_template('estructuras.html')

if __name__ == "__main__":
	app.run(debug=True)
