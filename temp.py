from flask import Flask,request,render_template, jsonify
import json
import Predict
import numpy as np
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/search": {"origins": "*"}, r"/evaluate": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/search',methods=['POST','GET', 'OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def search():
    print(request.is_json)
    if request.method == 'POST' or request.method == "GET":
        content = request.get_json()
    #print(content)
    result = Predict.getResults(content)
    #print(result)
    res = json.dumps(result)
    return res

@app.route('/evaluate',methods=['POST','GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@cross_origin(supports_credentials=True)
def test():
    if request.method == 'POST' or request.method == "GET" or request.method == "OPTIONS":
        data = request.get_json()
    vector = []
    list_of_attributes = ['vol','papers','work','c','html','css','bootstrap','mvc','java','ang','python','ml','nlp','tablaeu','R','stats','linux','windows','multithread']
    for e in list_of_attributes:
        if e in data:
            vector.append(int(data[e]))
        else:
            vector.append(0)

    lines = open('Data/hack_data.csv').readlines()
    X_arr = []
    y_arr = []

    for l in lines:
        a = l.split(",")
        templis = []
        for x in range(len(a)):
            if x < len(a)-1:
                templis.append(int(a[x]))
            else:
                y_arr.append(a[x][0:-1])

        X_arr.append(templis)

    backend = []
    frontend = []
    datasc = []
    datana = []
    systems = []
    for a in range(len(X_arr)):
        if y_arr[a] == "Back-End":
            backend.append(X_arr[a])
        elif y_arr[a] == "Front-End":
            frontend.append(X_arr[a])
        elif y_arr[a] == "Data-Science":
            datasc.append(X_arr[a])
        elif y_arr[a] == "Systems":
            systems.append(X_arr[a])
        else:
            datana.append(X_arr[a])


    similarityfront = 0
    similarityback = 0
    similarityds = 0
    similaritydana = 0
    systems_score = 0
    send_dict = {}

    for v in frontend:
        similarityfront += np.dot(np.array(vector), np.array(v))/ (np.linalg.norm(vector,2) * np.linalg.norm(v,2))

    similarityfront = (similarityfront * 100 )/len(frontend)


    for v in backend:
        similarityback += np.dot(np.array(vector), np.array(v))/ (np.linalg.norm(vector,2) * np.linalg.norm(v,2))

    similarityback = (similarityback * 100)/len(backend)


    for v in datasc:
        similarityds += np.dot(np.array(vector), np.array(v))/ (np.linalg.norm(vector,2) * np.linalg.norm(v,2))

    similarityds = (similarityds * 100) /len(datasc)


    for v in datana:
        similaritydana += np.dot(np.array(vector), np.array(v))/ (np.linalg.norm(vector,2) * np.linalg.norm(v,2))

    similaritydana = (similaritydana * 100 ) /len(datana)

    for v in systems:
        systems_score += np.dot(np.array(vector), np.array(v))/ (np.linalg.norm(vector,2) * np.linalg.norm(v,2))

    systems_score = (systems_score * 100 ) /len(systems)


    send_dict["Front"] = similarityfront
    send_dict["Back"] = similarityback
    send_dict["DataScience"] = similarityds
    send_dict["DataAnalytics"] = similaritydana
    send_dict["Systems"] = systems_score

    resu = jsonify(jsonobj=send_dict)
    return resu

if __name__ == "__main__":
    app.run(host="192.168.1.16", port=5000, debug=True)