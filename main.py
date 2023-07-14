from datetime import datetime
from flask import Flask, request, abort
from typing import List, Dict
from Cuenta import Cuenta

app = Flask(__name__)

BD: Dict[str, Cuenta] = dict()
cuenta1 = Cuenta("123", "Renato", 1000, ["456", "789"])
cuenta2 = Cuenta("456", "Joaquin", 2000, ["123", "789"])
cuenta3 = Cuenta("789", "Chachi", 3000, ["123", "456"])
BD["123"] = cuenta1
BD["456"] = cuenta2
BD["789"] = cuenta3


# Lista los contactos de una cuenta emisora
@app.route("/billetera/contactos")
def billetera_contactos():
    numero: str = request.args.get("minumero")

    respone = ''
    for num in BD.get(numero).contactos:
        respone += f"<p>{num}: {BD.get(num).nombre}<p>\n"

    return respone

# Realizar un pago a una cuenta destino
@app.route("/billetera/pagar")
def billetera_pagar():
    numero_origen = request.args.get("minumero")
    numero_destino = request.args.get("numerodestino")
    valor = float(request.args.get("valor"))

    cuenta = BD.get(numero_origen)
    fecha: str = cuenta.pagar(numero_destino, valor, BD)
    return f"Realizado en {fecha}"

# Consultar el historial de operaciones de una cuenta
@app.route("/billetera/historial")
def billetera_historial():
    numero: str = request.args.get("minumero")

    cuenta = BD.get(numero)
    return cuenta.historial(BD)

