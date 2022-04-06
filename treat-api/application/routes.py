from application import app
from flask import request, jsonify

treats = dict(Mila='Dreamies', Lilo='Live rat', Phoenix='tobacco')

@app.route('/treat', methods=['POST'])
def treat():
    cat_json = request.get_json()
    cat = cat_json["cat"]
    return jsonify(treat=treats[cat])