# TODO: Implementa el código del ejercicio

from abc import ABC, abstractmethod
from errores import *

class ReglaValidacion (ABC):


    @abstractmethod
    def es_valida(self):
        self._validar_longitud()
        self._contiene_numero()

    def __init__(self, _longitud_esperada, palabra):
        self._longitud_esperada = _longitud_esperada
        self.palabra = palabra

    def _validar_longitud(self):
        if len(self.palabra) > self._longitud_esperada:
            return True
        raise NoCumpleLongitudMinimaError


    def _contiene_mayuscula(self):
        respuesta = False
        for letra in self.palabra:
            if letra.isupper():
                   respuesta = True
                   break

        if not respuesta:
            raise NoTieneLetraMayusculaError

    def _contiene_minuscula(self):
        respuesta = False
        for letra in self.palabra:
            if letra.islower():
                respuesta = True
                break
        if not respuesta:
            raise NoTieneLetraMinusculaError

    def _contiene_numero(self):
        respuesta = False
        for letra in self.palabra:
            if letra.isdigit():
                respuesta = True
                break
        if not respuesta:
            raise NoTieneNumeroError

class Validador():

    def __init__(self, regla):
        self._regla = regla

    def es_valida(self, palabra):
        return self._regla.es_valida(palabra)
class ReglaValidacionGanimedes (ReglaValidacion):

    def contiene_caracter_especia(self):
        respuesta = False
        palabra_list = list(self.palabra)
        elementos = ['@','_','#','$','%']
        for letra in palabra_list:
            if letra in elementos:
                respuesta = True
                break
        if not respuesta:
            raise NoTieneCaracterEspecialError

    def __init__(self, palabra):
        self._longitud_esperada = 8
        self.palabra = palabra

        super().__init__(8, palabra)

    def es_valida(self):
        super().es_valida()
        super()._contiene_mayuscula()
        super()._contiene_minuscula()
        self.contiene_caracter_especia()
        return True

class ReglaValidacionCalisto (ReglaValidacion):

    def contiene_calisto(self):
        respuesta = False
        contador = 0
        start = self.palabra.lower().find("calisto")
        end = start + len("calisto")
        value = self.palabra[start:end]
        if "calisto" not in self.palabra.lower():
            raise NoTienePalabraSecretaError
        if value == "CALISTO":
            raise NoTienePalabraSecretaError
        for letra in value:
            if letra.isupper():
                contador += 1

            if contador == 2:
                respuesta = True
                break
        if not respuesta:
            raise NoTienePalabraSecretaError

    def __init__(self, palabra):
        self._longitud_esperada = 6
        self.palabra = palabra
        super().__init__(6, palabra)

    def es_valida(self):
        super().es_valida()
        self.contiene_calisto()
        return True

test = ReglaValidacionGanimedes( "h@oLa1olhkgguyrtdu")
test.es_valida()

test2 = ReglaValidacionCalisto( "FCaListo1")
test2.es_valida()