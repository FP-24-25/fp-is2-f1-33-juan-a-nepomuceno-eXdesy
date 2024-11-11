'''
Created on 11 nov 2024

@author: Fonix
'''

from __future__ import annotations
from typing import List, Tuple, TypeVar, Generic

E = TypeVar('E')
P = TypeVar('P')

class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[Tuple[E, P]] = []

    @staticmethod
    def of() -> Cola_prioridad[E, P]:
        return Cola_prioridad()

    def add(self, e: E, priority: P) -> None:
        # Encuentra la posición correcta en función de la prioridad
        index = self.__index_order(priority)
        self._elements.insert(index, (e, priority))

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e, priority in ls:
            self.add(e, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)[0]  # Elimina y devuelve el elemento de mayor prioridad

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def __index_order(self, priority: P) -> int:
        # Determina la posición de inserción en función de la prioridad
        for i, (_, p) in enumerate(self._elements):
            if priority < p:  # Menor valor de prioridad significa mayor prioridad
                return i
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def elements(self) -> List[E]:  # Cambiado a método en lugar de propiedad
        return [e for e, _ in self._elements]

    def __repr__(self) -> str:
        elements_str = ', '.join(f"({e}, {p})" for e, p in self._elements)
        return f"ColaPrioridad([{elements_str}])"

