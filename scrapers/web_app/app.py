from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    df = pd.read_csv('../wikitable/national_polls.csv')
    return render_template('home.html', data=df.to_html())

# Route for displaying the Spanish voting intentions table
@app.route('/spanish_voting_intentions')
def display_spanish_voting_intentions():
    df = pd.read_csv('scrapers/wikitable/spanish_voting_intentions.csv')
    return render_template('table.html', data=df.to_html())

# Route for the provincial elections page
@app.route('/provinces')
def provinces():
    return render_template('provinces.html')

# Route for the corrientes province page
@app.route('/provinces/corrientes')
def display_corrientes():
    return render_template('corrientes.html')

if __name__ == '__main__':
    app.run(debug=True)