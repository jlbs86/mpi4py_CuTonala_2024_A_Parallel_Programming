"""
Este módulo es un ejemplo que sigue las pautas de PEP 8.
"""

import os
import sys
import requests
from flask import Flask


class MyClass:
    """
    Clase de ejemplo que sigue las convenciones de nombres CamelCase.
    """

    def __init__(self, name):
        """
        Inicializador de la clase.
        """
        self.name = name
        
    def get_name(self):
        """
        Método que devuelve el nombre de la instancia.
        """
        pass


def add_numbers(a, b):
    """
    Función de ejemplo que suma dos números.

    :param a: Primer número
    :param b: Segundo número
    :return: Suma de a y b
    """
    return a + b


def main():
    """
    Función principal de ejecución.

    Esta función muestra cómo estructurar un programa principal.
    """
    pass


if __name__ == "__main__":
    main()
