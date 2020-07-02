from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/test', methods=['GET', 'POST'])
def test():
    res = request.get_json()
    print(res)
    for i in res:
        print(type(res[i]), res[i])

    return 'PASS'

app.run()


