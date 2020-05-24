from flask import Flask, jsonify, request

app = Flask(__name__)

from empleados import empleados

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/empleados', methods=['GET'])
def getEmpleados():

    return jsonify({'Empleados': empleados})

@app.route('/empleados/<string:empleado_nombre>', methods=['GET'])
def getEmpleado(empleado_nombre):
    
    for empleado in empleados:
        if empleado['FirstName'] == empleado_nombre:
            empleadoEncontrado=empleado
        #fijaros me va a devolver un diccionario
    print(type(empleadoEncontrado))
    if (len(empleadoEncontrado) > 0):
        return jsonify({'Empleado': empleadoEncontrado})
    else:
        return jsonify({'Mensaje': 'Empleado no encontrado'})

# Create Data Route
@app.route('/nuevo_empleado', methods=['POST'])
def addEmpleado():
    nuevo_empleado = {
        "FirstName" : request.json['FirstName'],
        "LastName" : request.json['LastName'],
        "ReportsTo" : request.json['ReportsTo'],
        "BirthDate" : request.json['BirthDate'],
        "HireDate" : request.json['HireDate'],
        "Address" : request.json['Address'],
        "City" : request.json['City'],
        "Province": request.json['Province'],
        "Country" : request.json['Country'],
        "PostalCode" : request.json['PostalCode'],
        "Phone" : request.json['Phone'],
        "Fax" : request.json['Fax'],
        "Email" : request.json['Email']
    }
    empleados.append(nuevo_empleado)
    return jsonify({'Mensaje': 'Empleado agregado correctamente', 'Empleados': empleados})

# Update Data Route
@app.route('/cambiar_empleado/<string:empleado_nombre>', methods=['PUT'])
def editEmpleado(empleado_nombre):
    for empleado in empleados:
        if empleado['FirstName'] == empleado_nombre:
            empleadoEncontrado=empleado  
    if (len(empleadoEncontrado) > 0):
        empleadoEncontrado[0]['FirstName'] = request.json['FirstName']
        empleadoEncontrado[0]['LastName'] = request.json['LastName']
        empleadoEncontrado[0]['ReportsTo'] = request.json['ReportsTo']
        empleadoEncontrado[0]['BirthDate'] = request.json['BirthDate']
        empleadoEncontrado[0]['HireDate'] = request.json['HireDate']
        empleadoEncontrado[0]['Address'] = request.json['Address']
        empleadoEncontrado[0]['City'] = request.json['City']
        empleadoEncontrado[0]['Province'] = request.json['Province']
        empleadoEncontrado[0]['Country'] = request.json['Country']
        empleadoEncontrado[0]['PostalCode'] = request.json['PostalCode']
        empleadoEncontrado[0]['Phone'] = request.json['Phone']
        empleadoEncontrado[0]['Fax'] = request.json['Fax']
        empleadoEncontrado[0]['Email'] = request.json['Email']
        return jsonify({
            'Mensaje': 'Empleado Modificado Correctamente',
            'Empleado': empleadoEncontrado[0]
        })
    return jsonify({'Mensaje': 'Empleado No Encontrado'})

# DELETE Data Route
@app.route('/eliminar_empleado/<string:empleado_nombre>', methods=['DELETE'])
def deleteEmpleado(empleado_nombre):
    for empleado in empleados:
        if empleado['FirstName'] == empleado_nombre:
            empleadoEncontrado=empleado
    if len(empleadoEncontrado) > 0:
        empleados.remove(empleadoEncontrado[0])
        return jsonify({
            'Mensaje': 'Empleado Borrado',
            'Empleados': empleados
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)