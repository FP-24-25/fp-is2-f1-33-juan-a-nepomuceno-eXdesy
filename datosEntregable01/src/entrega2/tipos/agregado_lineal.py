'''
Created on 11 nov 2024

@author: Dilyorbek Mukhiddinov
'''

from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Optional

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
    
    def contains(self, e: E) -> bool:
        for element in self._elements:
            if element == e:
                return True
        return False

    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        for element in self._elements:
            if func(element):
                return element
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        result = []
        for element in self._elements:
            if func(element):
                result.append(element)
        return result


