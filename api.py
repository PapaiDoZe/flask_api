from flask import Flask, jsonify, request

app = Flask(__name__)

clientes = [
    {
        "id": 1,
        "nome": 'Arthur Assimos',
        "idade": 27,
    },
    {
        "id": 2,
        "nome": 'Lucas Assimos',
        "idade": 26,
    },
]

"""Método get"""
@app.route("/clientes", methods=["GET"])
def get_clientes():
    return jsonify(clientes)

@app.route("/clientes/<int:id>", methods=["GET"])
def get_clientes_by_id(id):
    for cliente in clientes:
        if cliente.get("id") == id:
            return jsonify(cliente)
        elif cliente.get("id") != id:
            return jsonify("Esse cliente nao existe.")


"""MÉTODO POST"""

@app.route("/clientes", methods=["POST"])
def add_new_client():
    new_client = request.get_json()
    clientes.append(new_client)
    return jsonify(clientes)


"""METODO PUT"""

@app.route("/clientes/<int:id>", methods=["PUT"])
def edit_client_by_id(id):
    cliente_editado = request.get_json()
    for index, cliente in enumerate(clientes):
        if cliente.get("id") == id:
            clientes[index].update(cliente_editado)
            return jsonify(clientes[index])
        

"""METODO DELETE"""

@app.route("/clientes/<int:id>", methods=["DELETE"])
def delete_client_by_id(id):
    for index, cliente in enumerate(clientes):
        if cliente.get("id") == id:
            del clientes[index]
    return jsonify(clientes[index])


app.run(port=5000, host="localhost", debug=True)