'''
Created on 19 dec 2024

@author: Dilyorbek Mukhiddinov
'''

from __future__ import annotations
from src.entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from src.entrega3.Gen import Gen
from src.entrega3.Relacion_gen_a_gen import Relacion_gen_a_gen
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Red_genetica(E_grafo):
    genes_por_nombre: Dict[str, Gen]

    def __init__(self):
        super().__init__(graph_type=Graph_type.DIRECTED, weight=lambda e: 1.0, traverse_type=Traverse_type.FORWARD)
        self.genes_por_nombre = {}

    @staticmethod
    def of() -> Red_genetica:
        return Red_genetica()

    @staticmethod
    def parse(fichero_genes: str, fichero_relaciones: str) -> Red_genetica:
        red = Red_genetica()
        
        with open(fichero_genes, "r") as f:
            for linea in f:
                gen = Gen.parse(linea)
                red.add_vertex(gen)
                red.genes_por_nombre[gen.nombre] = gen

        with open(fichero_relaciones, "r") as f:
            for linea in f:
                relacion = Relacion_gen_a_gen.parse(linea)
                gen1 = red.genes_por_nombre[relacion.nombre_gen1]
                gen2 = red.genes_por_nombre[relacion.nombre_gen2]
                red.add_edge(gen1, gen2, relacion)

        return red

# Comprobación
if __name__ == "__main__":
    red = Red_genetica.parse("resources/genes.txt", "resources/red_genes.txt")
    print(red)