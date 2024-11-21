'''
Created on 11 nov 2024

@author: Dilyorbek Mukhiddinov
'''

from src.entrega2.tipos.pila import Pila

def test_pila():
    print("TEST DE PILA:\n")
    
    print("#" * 48)
    # Creación de una pila y adición de múltiples elementos
    print("Creación de una pila vacía y se añaden en este orden: 5, 4, -3, 2, 1, 47, 23")
    pila = Pila.of()
    elementos_a_agregar = [5, 4, -3, 2, 1, 47, 23]
    for elemento in elementos_a_agregar:
        pila.add(elemento)
    print(f"Resultado de la pila: {pila}\n")

    # Eliminar todos los elementos con remove_all()
    print("#" * 48)
    removed_elements = pila.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}\n")

if __name__ == '__main__':
    test_pila()