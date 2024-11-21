'''
Created on 20 oct 2024

@author: Dilyorbek Mukhiddinov
'''

from typing import List, Optional

# 6. Cuenta cuántas veces aparece una palabra en el archivo
def contar_palabra(fichero: str, sep: str, palabra: str) -> int:
    with open(fichero, 'r', encoding='utf-8') as f:
        contenido = f.read()
        palabras = contenido.split(sep)
        return palabras.count(palabra)

# 7. Devuelve una lista con las líneas que contienen una cadena de texto específica
def lineas_con_cadena(fichero: str, cad: str) -> List[str]:
    lineas = []
    with open(fichero, 'r', encoding='utf-8') as f:
        for linea in f:
            if cad in linea:
                lineas.append(linea.strip())
    return lineas

# 8. Encuentra todas las palabras únicas en el archivo
def palabras_unicas(fichero: str) -> List[str]:
    palabras = set()
    with open(fichero, 'r', encoding='utf-8') as f:
        for linea in f:
            palabras.update(linea.split())
    return list(palabras)

# 9. Devuelve la longitud promedio de las líneas en un archivo CSV
def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    with open(file_path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        if not lineas:
            return None
        longitudes = [len(linea.strip()) for linea in lineas]
        return sum(longitudes) / len(longitudes)
