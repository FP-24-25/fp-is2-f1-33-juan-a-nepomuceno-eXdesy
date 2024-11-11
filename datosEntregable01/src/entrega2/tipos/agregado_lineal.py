'''
Created on 11 nov 2024

@author: Fonix
'''

from __future__ import annotations
from typing import List, TypeVar, Generic, Optional

E = TypeVar('E')

class Agregado_lineal(Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0

    @property
    def elements(self) -> List[E]:
        return self._elements

    def add(self, e: E) -> None:
        raise NotImplementedError("Este método debe ser implementado en una subclase")

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements
