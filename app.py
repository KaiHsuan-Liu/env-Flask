from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

db = myclient['sth']
collect = db['record']

# SOMETHING = [
#     {
#         'title': 'Kai',
#         'comment': 'A handsome boy',
#         'check': True
#     },
#     {
#         'title': 'Mi',
#         'comment': 'A cute girl',
#         'check': False
#     }
# ]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/Sth', methods=['GET', 'POST'])
def sth():
    SOMETHING = []
    if request.method == 'POST':
        post_data = request.get_json()
        collect.insert_one(post_data)
    else:
        cursor = collect.find()
        for x in cursor:
            tmp = {}
            tmp['title'] = x['title']
            tmp['comment'] = x['comment']
            tmp['check'] = x['check']
            SOMETHING.append(tmp)

    return jsonify({
        'status': 'success',
        'something': SOMETHING
    })

if __name__ == '__main__':
    app.run()


