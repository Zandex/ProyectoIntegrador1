from flask import jsonify,request
from mysql.connector import Error
from db.database import cnx

class participante():
    global cursor
    cursor=cnx.cursor()

    def list():
        list_people=[]
        cursor.execute("select * from personas")
        
        rows =cursor.fetchall()
        columns =[i[0] for i in cursor.description]
        for  row in rows:
            registro = zip(columns,row)
            json=dict(registro)
            list_people.append(json)
        print(list_people)
        return jsonify(list_people)
        cnx.close

        #Show all registers

    def create(body):
        data = (body['cedula'],body['nombre'],body['actividad'],body['estrato'],body['foto'])
        sql = "INSERT INTO personas(cedula,nombre,actividad,estrato,foto) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(sql,data)
        cnx.commit()
        return {'estado':'Agregado'},200

if __name__ == "__main__":
    pass