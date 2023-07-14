from typing import List, Dict
from Operacion import Operacion
from datetime import datetime


class Cuenta:

    def __init__(self, numero: str, nombre:str, saldo: float, contactos: List[str]):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.historial_list: List[Operacion] = []

    def historial(self, BD) -> str:
        response = f"Saldo de {self.nombre}: {self.saldo}\nOperaciones de {self.nombre}:\n"
        for op in self.historial_list:
            if op.numero_emisor == self.numero:
                response += f"Pago realizado de  {op.valor} a {BD.get(op.numero_destino).nombre}\n"
            else:
                response += f"Pago recibido de {op.valor} de {BD.get(op.numero_emisor).nombre}\n"
        return response

    def pagar(self, destino: str, valor: float, BD) -> str:
        if valor > self.saldo:
            return "No tiene saldo suficiente"
        if destino not in self.contactos:
            return "No es un contacto"
        if valor < 0:
            return "El valor no es correcto"
        self.saldo -= valor
        op = Operacion(self.numero, destino, f"{datetime.now().date()}", valor)
        self.historial_list.append(op)

        BD.get(destino).saldo += valor
        BD.get(destino).historial_list.append(op)

        return self.historial_list[-1].fecha

