'''
Created on 11 nov 2024

@author: Dilyorbek Mukhiddinov
'''

from __future__ import annotations
from typing import Callable, TypeVar, Generic
from src.entrega2.tipos.agregado_lineal import *

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada_sin_repeticion(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order: Callable[[E], R] = order

    @staticmethod
    def of(order: Callable[[E], R]) -> Lista_ordenada_sin_repeticion[E, R]:
        return Lista_ordenada_sin_repeticion(order)

    def __index_order(self, e: E) -> int:
        # Encuentra la posición de inserción para mantener el orden, si el elemento no existe ya
        for i, element in enumerate(self._elements):
            if self._order(e) < self._order(element):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        # Solo añadir si el elemento no está ya en la lista
        if e not in self._elements:
            index = self.__index_order(e)
            self._elements.insert(index, e)

    def __repr__(self) -> str:
        elements_str = ', '.join(str(e) for e in self._elements)
        return f"ListaOrdenadaSinRepeticion([{elements_str}])"
