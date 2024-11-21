'''
Created on 11 nov 2024

@author: Dilyorbek Mukhiddinov
'''

from __future__ import annotations
from typing import TypeVar
from src.entrega2.tipos.agregado_lineal import *

E = TypeVar('E')

class Pila(Agregado_lineal[E]):
    @staticmethod
    def of() -> Pila[E]:
        return Pila()

    def add(self, e: E) -> None:
        # Añade el elemento al principio de la pila
        self._elements.insert(0, e)

    def __repr__(self) -> str:
        elements_str = ', '.join(str(e) for e in self._elements)
        return f"Pila([{elements_str}])"
