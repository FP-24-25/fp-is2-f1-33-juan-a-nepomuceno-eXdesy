'''
Created on 19 dec 2024

@author: Dilyorbek Mukhiddinov
'''

from __future__ import annotations    
from dataclasses import dataclass

@dataclass(frozen=True)
class Relacion_gen_a_gen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> Relacion_gen_a_gen:
        assert -1 <= conexion <= 1, "La conexión debe estar entre -1 y 1"
        return Relacion_gen_a_gen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(linea: str) -> Relacion_gen_a_gen:
        partes = linea.strip().split(",")
        return Relacion_gen_a_gen.of(partes[0], partes[1], float(partes[2]))

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.conexion < -0.75

# Comprobación
if __name__ == "__main__":
    linea = "TP53,KRAS,0.7"
    relacion = Relacion_gen_a_gen.parse(linea)
    print(relacion)
    print("Coexpresados:", relacion.coexpresados)
    print("Antiexpresados:", relacion.antiexpresados)
