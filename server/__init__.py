from flask import Flask
from flask_cors import CORS
from flask import request
import json
import Predict_test2

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def hello():
    p = Predict_test2.Predict()
    p.action(json.loads(str(request.data).split('\'')[1])['data'])
    return {"result":p.result, "test":p.test}

if __name__ == "__main__":
    app.run()

@app.errorhandler(404) 
def page_not_found(error): 
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.errorhandler(500) 
def page_not_found(error): 
    return '에러..'


