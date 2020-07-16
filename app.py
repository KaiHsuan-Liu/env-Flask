from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo
import uuid

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

db = myclient['sth']
collect = db['record']

def remove_sth(sth_id):
    myquery = { "id": sth_id }
    mydoc = collect.find_one(myquery)
    if mydoc == None:
        return False
    else:
        collect.delete_one(myquery)
        return True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/Sth', methods=['GET', 'POST'])
def sth():
    SOMETHING = []
    if request.method == 'POST':
        post_data = request.get_json()
        post_data['id'] = uuid.uuid4().hex
        collect.insert_one(post_data)
    else:
        cursor = collect.find()
        for x in cursor:
            print(x)
            tmp = {}
            tmp['id'] = x['id']
            tmp['title'] = x['title']
            tmp['comment'] = x['comment']
            tmp['check'] = x['check']
            SOMETHING.append(tmp)
    return jsonify({
        'status': 'success',
        'something': SOMETHING
    })

@app.route('/Sth/<sth_id>', methods=['PUT', 'DELETE'])
def single_Sth(sth_id):
    if request.method == 'PUT':
        post_data = request.get_json()
        print(post_data)
        myquery = { "id": sth_id }
        newvalues = { "$set": post_data }
        collect.update_one(myquery, newvalues)

    if request.method == 'DELETE':
        remove_sth(sth_id)

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run()


