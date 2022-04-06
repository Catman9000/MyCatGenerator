from application import app, db
from application.models import Results
from flask import render_template
import requests

@app.route('/')
def index():
    cat = requests.get('http://cat-api:5000/cat')
    treat = requests.post('http://treat-api:5000/noise', json=cat.json())
    db.session.add(Results(cat=cat.json()["cat"], treat=treat.json()["treat"]))
    db.session.commit()
    cattreat = Results.query.all()
    return render_template('index.html', results = results)