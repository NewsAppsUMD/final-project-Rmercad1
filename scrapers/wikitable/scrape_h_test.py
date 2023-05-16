from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/spanish_voting_intentions')
def display_spanish_voting_intentions():
    df = pd.read_csv('scrapers/wikitable/spanish_voting_intentions.csv')
    return render_template('table.html', data=df.to_html())

if __name__ == '__main__':
    app.run()