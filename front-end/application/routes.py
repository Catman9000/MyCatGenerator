from application import app, db
from application.models import results
from flask import render_template
import requests

@app.route('/')
def index():
    cat = requests.get('http://cat-api:5000/cat')
    treat = requests.post('http://treat-api:5000/treat', json=cat.json())
    db.session.add(results(cat=cat.json()["cat"], treat=treat.json()["treat"]))
    db.session.commit()
    treatnames = results.query.all()
    catnames = results.query.all()
    return render_template('index.html', treatnames = treatnames, catnames = catnames)