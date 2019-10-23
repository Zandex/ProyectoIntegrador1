from flask import Flask,jsonify,request
from flask_cors import CORS
from Controles.participante import participante

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def test:
    return "HOLA estas en el API"

@app.route('/getpeople',methods=['GET'])
def getdata():
    return participante.list()

@app.route('/setpeople',methods=['POST'])
def setpeople():
    body=request.json
    return participante.create(body)

#app.run(port=5000,debug=True)
