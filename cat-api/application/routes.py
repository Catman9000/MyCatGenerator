from application import app
from flask import jsonify
from random import choice

cats = ['Mila', 'Lilo', 'Phoenix']

@app.route('/cat', methods=['GET'])
def get_cat():
    cat = choice(cats)
    return jsonify(cat=cat)