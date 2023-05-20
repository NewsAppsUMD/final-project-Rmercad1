from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the provincial elections page
@app.route('/provinces')
def provinces():
    return render_template('provinces.html')

# Route for the corrientes province page
@app.route('/provinces/corrientes')
def display_corrientes():
    return render_template('corrientes.html')

# Route for the Tucuman province page
@app.route('/provinces/tucuman')
def display_tucuman():
    return render_template('tucuman.html')

@app.route('/provinces/cordoba')
def display_cordoba():
    return render_template('cordoba.html')

@app.route('/provinces/formosa')
def display_formosa():
    return render_template('formosa.html')

@app.route('/provinces/chubut')
def display_chubut():
    return render_template('chubut.html')

@app.route('/provinces/santacruz')
def display_santacruz():
    return render_template('santacruz.html')

@app.route('/provinces/santafe')
def display_santafe():
    return render_template('santafe.html')

@app.route('/provinces/chaco')
def display_chaco():
    return render_template('chaco.html')

@app.route('/provinces/mendoza')
def display_mendoza():
    return render_template('mendoza.html')

@app.route('/provinces/caba')
def display_caba():
    return render_template('caba.html')

@app.route('/provinces/catamarca')
def display_catamarca():
    return render_template('catamarca.html')

@app.route('/provinces/entrerios')
def display_entrerios():
    return render_template('entrerios.html')

@app.route('/provinces/buenosaires')
def display_buenosaires():
    return render_template('buenosaires.html')

@app.route('/provinces/sanluis')
def display_sanluis():
    return render_template('sanluis.html')

if __name__ == '__main__':
    app.run(debug=True)

