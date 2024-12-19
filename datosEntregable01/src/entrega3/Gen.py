'''
Created on 19 dec 2024

@author: Dilyorbek Mukhiddinov
'''

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> Gen:
        assert num_mutaciones >= 0, "El número de mutaciones debe ser mayor o igual a cero"
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(linea: str) -> Gen:
        partes = linea.strip().split(",")
        return Gen.of(partes[0], partes[1], int(partes[2]), partes[3])

    def __str__(self) -> str:
        return f"{self.nombre}: ({self.tipo},{self.num_mutaciones},{self.loc_cromosoma})"

# Comprobación
if __name__ == "__main__":
    linea = "TP53,supresor tumoral,256,17p13.1"
    gen = Gen.parse(linea)
    print(gen)
