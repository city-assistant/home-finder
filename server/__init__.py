from flask import Flask
import Predict
app = Flask(__name__)

@app.route("/")
def hello():
    p = Predict.Predict()
    p.action()
    result = p.result
    return str(result)

if __name__ == "__main__":
    app.run()

@app.errorhandler(404) 
def page_not_found(error): 
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.errorhandler(500) 
def page_not_found(error): 
    return '에러..'


