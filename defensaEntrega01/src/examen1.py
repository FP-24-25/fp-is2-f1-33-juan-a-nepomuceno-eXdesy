'''
Created on 24 oct 2024

@author: Fonix
'''

import math
from typing import List, Tuple
from collections import Counter
import string

def P2(n: int, k: int, i: int = 1):
    try:
        assert n >= k, "El valor n debe ser mayor o igual que el valor k"
        assert n > 0, "El valor n debe ser mayor que 0"
        assert i > 0, "El valor i debe ser mayor que 0"
        assert k > 0, "El valor k debe ser mayor que 0"
        assert i < k + 1, "El valor i debe ser menor que k+1"

        producto = 1
        for j in range(k - 1):
            producto *= (n - j + 1)
        return producto
    except AssertionError as ae:
        print(f"Error de aserción: {ae}")
    except Exception as e:
        print(f"Error inesperado: {e}")

print('\n********** EJERCICIO P2 **********')
valor_n = int(input("Introduce el valor de n: "))
valor_k = int(input("Introduce el valor de k: "))
print("El resultado es: " + str(P2(valor_n, valor_k)) + "\n")

def C2(n: int, k: int):
    try:
        assert n > k, "El valor n debe ser mayor que el valor k"
        assert n > 0, "El valor n debe ser mayor que 0"
        assert k > 0, "El valor k debe ser mayor que 0"

        return math.comb(n, k + 1)
    except AssertionError as ae:
        print(f"Error de aserción: {ae}")
    except Exception as e:
        print(f"Error inesperado: {e}")

print('\n********** EJERCICIO C2 **********')
valor_n = int(input("Introduce el valor de n: "))
valor_k = int(input("Introduce el valor de k: "))
print("El resultado es: " + str(C2(valor_n, valor_k)) + "\n")


def S2(n: int, k: int):
    try:
        assert n >= k, "El valor n debe ser mayor o igual que el valor k"
        assert n > 0, "El valor n debe ser mayor que 0"
        assert k > 0, "El valor k debe ser mayor que 0"
        
        factorial = math.factorial(k) / (n * math.factorial(k + 2))
        
        sumatorio = 0
        for i in range(k + 1):
            coef_signo = (-1) ** i
            comb = math.factorial(k) // (math.factorial(i) * math.factorial(n - i))
            term = (k - i) ** (n + 1)
            sumatorio += coef_signo * comb * term
        
        resultado = factorial * sumatorio
        return resultado
    except AssertionError as ae:
        print(f"Error de aserción: {ae}")
    except Exception as e:
        print(f"Error inesperado: {e}")

print('\n********** EJERCICIO S2 **********')
valor_n = int(input("Introduce el valor de n: "))
valor_k = int(input("Introduce el valor de k: "))
print("El resultado es: " + str(S2(valor_n, valor_k)) + "\n")


def palabrasMasComunes(fichero: str, n: int = 5) -> List[Tuple[str, int]]:
    assert n > 1, "El parámetro n debe ser mayor que 1"
    
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            texto = f.read()
        
        texto = texto.lower().translate(str.maketrans("", "", string.punctuation))
        
        palabras = texto.split()
        
        contador = Counter(palabras)
        
        palabras_comunes = contador.most_common(n)
        
        return palabras_comunes
    
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {fichero}")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

palabras_comunes = palabrasMasComunes('archivo_palabras.txt', 5)
print('\n********** PALABRAS MAS COMUNES **********')
print(palabras_comunes)


    