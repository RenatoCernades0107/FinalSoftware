import pytest
from typing import Dict
from Cuenta import Cuenta
from Operacion import Operacion

class TestClass:
    def setup_method(self):
        self.BD = dict()
        self.cuenta1 = Cuenta("123", "Renato", 1000, ["456", "789"])
        self.cuenta2 = Cuenta("456", "Joaquin", 2000, ["123", "789"])
        self.cuenta3 = Cuenta("789", "Chachi", 3000, ["123", "456"])
        self.BD["123"] = self.cuenta1
        self.BD["456"] = self.cuenta2
        self.BD["789"] = self.cuenta3
    def test_historial_exito(self):
        """
        Testea el metodo historial de la clase Cuenta hacinedo un pago y viendolo en el historial.
        Se espera que el resultado sea el esperado.
        """
        expected_result = "Saldo de Renato: 1100\nOperaciones de Renato:\nPago recibido de 100 de Joaquin\n"

        self.cuenta2.pagar("123", 100, self.BD)
        result = self.cuenta1.historial(self.BD)

        assert result == expected_result

    def test_historial_exito_segundo(self):
        """
        Testea el metodo historial de la clase Cuenta hacinedo un pago y viendolo en el historial,
        en este caso, como se han hecho pagos, el historial está vacío.
        """
        expected_result = "Saldo de Renato: 1000\nOperaciones de Renato:\n"

        result = self.cuenta1.historial(self.BD)
        assert result == expected_result

    def test_pagar_exito(self):
        """
        Testea el metodo pagar de la clase Cuenta, haciendo un pago y viendo que el saldo de la cuenta destino.
        Se espera que el resultado sea el esperado.
        """
        expected_result = 2100
        self.cuenta1.pagar("456", 100, self.BD)

        assert self.BD.get("456").saldo == expected_result

    def test_pagar_exito_segundo(self):
        """
        Testea el metodo pagar de la clase Cuenta, haciendo dos pagos y viendo que el saldo de la cuenta destino.
        Se espera que el resultado sea el esperado.
        """
        expected_result = 2200
        self.cuenta1.pagar("456", 100, self.BD)
        self.cuenta1.pagar("456", 100, self.BD)

        assert self.BD.get("456").saldo == expected_result


    def test_pagar_sin_saldo(self):
        """
        Testea el metodo pagar de la clase Cuenta, haciendo un pago.
        Se espera ver un error que indique que el saldo no es suficiente.
        """
        expected_result = "No tiene saldo suficiente"
        result = self.cuenta1.pagar("456", 10000, self.BD)

        assert result == expected_result

    def test_pagar_sin_contacto(self):
        """
        Testea el metodo pagar de la clase Cuenta, haciendo un pago.
        Se espera ver un error que indique que el contacto no existe.
        """
        expected_result = "No es un contacto"
        result = self.cuenta1.pagar("000", 100, self.BD)

        assert result == expected_result

    def test_pagar_negativo(self):
        """
        Testea el metodo pagar de la clase Cuenta, haciendo un pago.
        Se espera ver un error que indique que el valor no es correcto.
        """
        expected_result = "El valor no es correcto"
        result = self.cuenta1.pagar("456", -100, self.BD)

        assert result == expected_result