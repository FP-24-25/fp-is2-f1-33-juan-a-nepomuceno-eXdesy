'''
Created on 10 dec 2024

@author: Dilyorbek Mukhiddinov
'''

from ..Red_social import *
from ..Recorrido_en_profundidad import Recorrido_en_profundidad

if __name__ == '__main__':
    rrss: Red_social = Red_social.parse('../resources/usuarios.txt', '../resources/relaciones.txt')
    if rrss:
        r:Recorrido_en_profundidad[Usuario,Relacion] = Recorrido_en_profundidad.of(rrss)
        
        source:Usuario = rrss.usuarios_dni['25143909I']
        
        r.traverse(source)
        
        target: Usuario =  rrss.usuarios_dni['76929765H']
        
        camino = r.path_to_origin(source)
        # Mostrar el resultado
        if target in camino:
            print(f"El camino más corto desde {source.dni} hasta {target.dni} es: {camino}")
            print(f"La distancia mínima es: {r.path_weight(target)} pasos.")
        else:
            print(f"No hay conexión directa entre {source.dni} y {target.dni}.")
    else:
        print("Error al crear la red social.")