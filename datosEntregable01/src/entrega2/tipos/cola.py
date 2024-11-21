'''
Created on 11 nov 2024

@author: Dilyorbek Mukhiddinov
'''

from __future__ import annotations
from typing import TypeVar
from src.entrega2.tipos.agregado_lineal import *

E = TypeVar('E')

class Cola(Agregado_lineal[E]):
    @staticmethod
    def of() -> Cola[E]:
        return Cola()

    def add(self, e: E) -> None:
        # Añade el elemento al final de la cola
        self._elements.append(e)

    def __repr__(self) -> str:
        elements_str = ', '.join(str(e) for e in self._elements)
        return f"Cola([{elements_str}])"
