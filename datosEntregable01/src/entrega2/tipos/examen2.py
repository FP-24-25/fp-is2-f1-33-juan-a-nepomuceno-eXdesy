'''
Created on 21 nov 2024

@author: Dilyorbek Mukhiddinov
'''

from __future__ import annotations
from typing import TypeVar
# No se por que, pero sin ruta da error de que el metodo Agregado_lineal no es indefinido aunque envia al metodo.
from src.entrega2.tipos.agregado_lineal import Agregado_lineal

E = TypeVar('E')

class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        assert capacidad > 0, "La capacidad debe ser mayor que 0"
        self._capacidad = capacidad

    @property
    def capacidad(self) -> int:
        return self._capacidad

    @property
    def is_full(self) -> bool:
        return self.size >= self._capacidad

    def add(self, e: E) -> None:
        if self.is_full:
            raise OverflowError("La cola está llena")
        self._elements.append(e)

    @classmethod
    def of(cls, capacidad: int) -> ColaConLimite[E]:
        return cls(capacidad)

# TEST
import unittest

class TestColaConLimite(unittest.TestCase):
    def setUp(self):
        self.cola = ColaConLimite.of(3)

    def test_add_element(self):
        # Intento agregar elementos a la cola
        self.cola.add("Tarea 1")
        self.cola.add("Tarea 2")
        self.cola.add("Tarea 3")
        self.assertEqual(self.cola.size, 3)
        self.assertEqual(self.cola.elements, ["Tarea 1", "Tarea 2", "Tarea 3"])

    def test_add_overflow(self):
        # Verifico que pasaria si intento agregar mas elementos a la cola llena
        self.cola.add("Tarea 1")
        self.cola.add("Tarea 2")
        self.cola.add("Tarea 3")
        with self.assertRaises(OverflowError) as context:
            self.cola.add("Tarea 4")
        self.assertEqual(str(context.exception), "La cola está llena")

    def test_remove_element(self):
        # Elimino todos los elementos segun el orden
        self.cola.add("Tarea 1")
        self.cola.add("Tarea 2")
        self.cola.add("Tarea 3")
        self.assertEqual(self.cola.remove(), "Tarea 1")
        self.assertEqual(self.cola.size, 2)
        self.assertEqual(self.cola.elements, ["Tarea 2", "Tarea 3"])

    def test_remove_empty(self):
        # Pruebo eliminar elementos de cola vacia
        with self.assertRaises(AssertionError) as context:
            self.cola.remove()
        self.assertEqual(str(context.exception), "El agregado está vacío")

    def test_is_full(self):
        # A ver si la cola esta llena
        self.assertFalse(self.cola.is_full)
        self.cola.add("Tarea 1")
        self.cola.add("Tarea 2")
        self.assertFalse(self.cola.is_full)
        self.cola.add("Tarea 3")
        self.assertTrue(self.cola.is_full)

    def test_empty_queue(self):
        # Verifico que una cola recién creada está vacía
        self.assertTrue(self.cola.is_empty)
        self.assertEqual(self.cola.size, 0)

    def test_add_and_remove_all(self):
        # Inento agregar varios elementos y luego eliminarlos todos
        self.cola.add("Tarea 1")
        self.cola.add("Tarea 2")
        self.cola.add("Tarea 3")
        removed_elements = self.cola.remove_all()
        self.assertEqual(removed_elements, ["Tarea 1", "Tarea 2", "Tarea 3"])
        self.assertTrue(self.cola.is_empty)

    def test_invalid_capacity(self):
        # No se puede crear una cola con capacidad <= 0
        with self.assertRaises(AssertionError) as context:
            ColaConLimite.of(0)
        self.assertEqual(str(context.exception), "La capacidad debe ser mayor que 0")

if __name__ == "__main__":
    unittest.main()

    
