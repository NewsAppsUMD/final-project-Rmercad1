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

@app.route('/provinces/corrientes2')
def display_corrientes2():
    return render_template('corrientes2.html')

@app.route('/provinces/cordoba')
def display_cordoba():
    return render_template('cordoba.html')

@app.route('/provinces/formosa')
def display_formosa():
    return render_template('formosa.html')

@app.route('/provinces/chubut')
def display_chubut():
    return render_template('chubut.html')

@app.route('/provinces/santafe2')
def display_santafe2():
    return render_template('santafe2.html')

@app.route('/provinces/santacruz2')
def display_santacruz2():
    return render_template('santacruz2.html')

@app.route('/provinces/chaco')
def display_chaco():
    return render_template('chaco.html')

@app.route('/provinces/tucumanpolls')
def display_tucumanpolls():
    return render_template('tucumanpolls.html')

@app.route('/provinces/mendoza')
def display_mendoza():
    return render_template('mendoza.html')

@app.route('/provinces/tucumanprovincepolls')
def display_tucumanprovincepolls():
    return render_template('tucumanprovincepolls.html')

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
