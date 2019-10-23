from flask import Flask,jsonify,request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)   #compartir recursos a diferentes origenes , comunicacion entre servidores
#08
tipo_datos={'sensor':'TSL2561','variable:':'LUZ SOLAR','unidades':'Lux' }

datos=[
    {'fecha':'2019-08-9 11:24:32',**tipo_datos,'valor':40.0},
    {'fecha':'2019-08-9 12:24:32',**tipo_datos,'valor':2500.0},
    {'fecha':'2019-08-10 13:24:32',**tipo_datos,'valor':1600.0},
    {'fecha':'2019-08-10 14:23:32',**tipo_datos,'valor':20000.0},
    {'fecha':'2019-08-11 16:24:32',**tipo_datos,'valor':33000.0},
    {'fecha':'2019-08-12 17:24:32',**tipo_datos,'valor':1000.0},
    {'fecha':'2019-08-12 18:24:32',**tipo_datos,'valor':37000.0},
    {'fecha':'2019-08-13 19:24:32',**tipo_datos,'valor':5000.0}
]

@app.route('/')
def get():
    return jsonify(tipo_datos)

@app.route('/datos',methods = ['GET'])
def getAll():
    return jsonify(datos)

@app.route('/datos/fecha/<fecha>',methods = ['GET'])
def getByFecha(fecha):
    res=[]
    for x in datos:
        if((x['fecha']).find(fecha)>=0):
            res.append(x)
            
    return jsonify(res)

@app.route('/datos/<porcent>',methods = ['GET'])
def getspecial(porcent):
    datatmp=[]
    datares=[]
    datatmp=datos
    datatmp.sort(key=lambda x: x['valor'], reverse=True)
    ndatos=(len(datatmp)*float(porcent))
    for x in range(int(ndatos)):
        datares.append(datatmp[x])
    return jsonify(datares)



@app.route('/datos', methods = ['POST'])
def postdate():
    now = datetime.now()
    body = request.json
    body['fecha'] =datetime.strftime(now,'%Y-%m-%d %H:%M:%S')
    datos.append({**body,**tipo_datos})
    return jsonify(datos)

@app.route('/datos/fecha/<fecha>', methods = ['DELETE'])
def delete(fecha):
    x=len(datos)
    index=0
    while(index<x-1):
        print(datos[index])
        if(str(datos[index]['fecha']).find(fecha)>=0):
            datos.pop(index)  
            x=x-1
        else:
            index=index+1     
    return jsonify(datos)

@app.route('/datos/fecha/<fecha>', methods = ['PUT'])
def put(fecha):
    body=request.json
    for x in datos:
        if((x['fecha']).find(fecha)>=0):
            x['valor']=body['valor']
            return x          
    return jsonify(datos)

app.run(debug=True, port=5000) #run app in debug mode on port 5000