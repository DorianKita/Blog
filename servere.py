import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.datetime.now().year
    return render_template('index.html', year=year)

@app.route('/guess/<name>')
def guess(name):
    gender_data = requests.get(url=f'https://api.genderize.io?name={name}').json()['gender']
    age_data = requests.get(url = f'https://api.agify.io?name={name}').json()['age']

    return render_template('guess.html', name=name, sex = gender_data, age = age_data)


if __name__ == '__main__':
    app.run(debug=True)
