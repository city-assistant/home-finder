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

