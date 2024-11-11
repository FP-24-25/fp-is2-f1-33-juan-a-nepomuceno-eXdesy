'''
Created on 11 nov 2024

@author: Fonix
'''

from src.entrega2.tipos.lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

def test_lista_ordenada_sin_repeticion():
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN:\n")
    
    print("#" * 48)
    # Creación de una lista con criterio de orden lambda x: -x
    print("Creación de una lista con criterio de orden lambda x: -x")
    lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)
    elementos_a_agregar = [23, 47, 47, 1, 2, -3, 4, 5]
    for elemento in elementos_a_agregar:
        lista.add(elemento)
    print(f"Se añade en este orden: {', '.join(map(str, elementos_a_agregar))}")
    print(f"Resultado de la lista ordenada sin repetición: {lista}\n")

    # Eliminar el primer elemento con remove()
    print("#" * 48)
    removed_element = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed_element}\n")

    # Eliminar todos los elementos con remove_all()
    print("#" * 48)
    removed_elements = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}\n")

    # Añadir y comprobar posiciones correctas, evitando duplicados
    print("#" * 48)
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(0)  # Intento de duplicado, no debería añadirse
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}\n")

if __name__ == '__main__':
    test_lista_ordenada_sin_repeticion()
