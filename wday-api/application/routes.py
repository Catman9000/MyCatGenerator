from application import app
from flask import request, jsonify

wdays = dict(Mila='Sunday', Lilo='Monday', Phoenix='Wednesday')

@app.route('/wday', methods=['POST'])
def wday():
    cat_json = request.get_json()
    cat = cat_json["cat"]
    return jsonify(wday=wdays[cat])