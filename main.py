from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCandidato import ControladorCandidato

app = Flask(__name__)
cors = CORS(app)


## Ejecutando controlador Candidato
miControladorCandidato=ControladorCandidato()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running: " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])



##peticiones del servidor respecto a Candidadto
@app.route("/candidatos",methods=['GET'])
def getEstudiantes():
    json=miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)