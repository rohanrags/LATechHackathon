from flask import Flask,request,render_template, jsonify
import json
import Predict
import numpy as np

app = Flask(__name__)


@app.route('/search',methods=['POST'])
def bacon():
    print(request.is_json)
    content = request.get_json()
    #print(content)
    result = Predict.getResults(content)
    #print(result)
    return json.dumps(result)

@app.route('/evaluate',methods=['POST','GET'])
def test():
    if request.method == 'POST' or request.method == "GET":
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


    send_dict["Front-End"] = similarityfront
    send_dict["Back-End"] = similarityback
    send_dict["Data-Science"] = similarityds
    send_dict["Data-Analytics"] = similaritydana
    send_dict["Systems"] = systems_score

    return jsonify(jsonobj=send_dict)

if __name__ == "__main__":
    app.run(debug=True)