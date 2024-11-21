'''
Created on 11 nov 2024

@author: Dilyorbek Mukhiddinov
'''

from src.entrega2.tipos.lista_ordenada import Lista_ordenada

def test_lista_ordenada():
    print("TEST DE LISTA ORDENADA:\n")
    
    print("#" * 48)
    # Creación de una lista con criterio de orden lambda x: x
    print("Creación de una lista con criterio de orden lambda x: x")
    lista = Lista_ordenada.of(lambda x: x)
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Se añade en este orden: 3, 1, 2")
    print(f"Resultado de la lista: {lista}\n")

    # Eliminar el primer elemento con remove()
    print("#" * 48)
    removed_element = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed_element}\n")

    # Eliminar todos los elementos con remove_all()
    print("#" * 48)
    removed_elements = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}\n")

    # Añadir y comprobar posiciones correctas
    print("#" * 48)
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}\n")

if __name__ == '__main__':
    test_lista_ordenada()

