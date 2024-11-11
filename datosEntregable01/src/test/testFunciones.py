'''
Created on 20 oct 2024

@author: Fonix
'''

import unittest
from src.funciones.funciones import *

class TestFunciones(unittest.TestCase):

    def test_producto_n_k(self):
        resultado = producto_n_k(5, 3)
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 1:")
        print(f"El producto de 4 y 2 es: {resultado}")
        self.assertEqual(resultado, 360)

    def test_producto_geometrico(self):
        resultado = producto_geometrico(3, 5, 2)
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 2:")
        print(f"El producto de la secuencia geométrica con a1 = 3, r = 5 y k = 2 es: {resultado}")
        self.assertEqual(resultado, 45)

    def test_combinatorio(self):
        resultado = combinatorio(4, 2)
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 3:")
        print(f"El número combinatorio de 4 y 2 es: {resultado}")
        self.assertEqual(resultado, 6)

    def test_S_n_k(self):
        resultado = S_n_k(4, 2)
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 4:")
        print(f"El número S(n,k) siendo n = 4 y k = 2 es: {resultado}")
        self.assertAlmostEqual(resultado, 22.5, places=1)

    def test_metodo_newton(self):
        f = lambda x: 2 * x ** 2
        df = lambda x: 4 * x
        resultado = metodo_newton(f, df, 3, 0.001)
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 5:")
        print(f"Resultado de la función 5 con a = 3 y e = 0.001, f(x) = 2x^2 y f'(x) = 4x: {resultado}")
        self.assertAlmostEqual(resultado, 0.01171875, places=6)


if __name__ == '__main__':
    unittest.main()



