from application import app
from flask import jsonify
from random import choice

cats = ['Mila', 'Lilo', 'Phoenix', 'Cookie', 'Cinnamon', 'Chocolate', 'Oreo', 'Steve', 'Mouse']

@app.route('/cat', methods=['GET'])
def get_cat():
    cat = choice(cats)
    return jsonify(cat=cat)