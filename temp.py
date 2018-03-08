from flask import Flask,request,render_template
import json
import Predict

app = Flask(__name__)


@app.route('/bacon',methods=['POST'])
def bacon():
    print(request.is_json)
    content = request.get_json()
    #print(content)
    result = Predict.getResults(content)
    #print(result)
    return json.dumps(result)


if __name__ == "__main__":
    app.run(debug=True)