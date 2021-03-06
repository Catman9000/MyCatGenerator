from application import app
from flask import request, jsonify

treats = dict(Mila='Dreamies treats', Lilo='Live rat', Phoenix='Felix treats', Cookie='Whiskas', Cinnamon='dead rat', Chocolate='garfield', Oreo='lasange', Steve='tuna', Mouse='curry')

@app.route('/treat', methods=['POST'])
def treat():
    cat_json = request.get_json()
    cat = cat_json["cat"]
    return jsonify(treat=treats[cat])