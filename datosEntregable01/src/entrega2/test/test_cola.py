'''
Created on 11 nov 2024

@author: Fonix
'''

from src.entrega2.tipos.cola import Cola

def test_cola():
    print("TEST DE COLA:\n")
    
    print("#" * 48)
    # Creación de una cola y adición de múltiples elementos con un solo método
    print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
    cola = Cola.of()
    elementos_a_agregar = [23, 47, 1, 2, -3, 4, 5]
    cola.add_all(elementos_a_agregar)
    print(f"Resultado de la cola: {cola}\n")

    # Eliminar todos los elementos con remove_all()
    print("#" * 48)
    removed_elements = cola.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}\n")

if __name__ == '__main__':
    test_cola()

