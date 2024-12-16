'''
Created on 20 oct 2024

@author: Dilyorbek Mukhiddinov
'''

import unittest
from src.entrega1.lecturas import *

class TestLecturas(unittest.TestCase):

    def test_contar_palabra(self):
        resultado = contar_palabra(r'C:\Users\Admin\eclipse-workspace\Dilior_Entregable\datosEntregable01\src\resources\lin_quijote.txt', " ", "Quijote")
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 6:")
        print(f"El número de veces que aparece la palabra quijote en el fichero resources/lin_quijote.txt es: {resultado}")
        self.assertEqual(resultado, 1)

    def test_lineas_con_cadena(self):
        resultado = lineas_con_cadena(r"C:\Users\Admin\eclipse-workspace\Dilior_Entregable\datosEntregable01\src\resources\lin_quijote.txt", "Quijote")
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 7:")
        print(f"Las líneas en las que aparece la palabra quijote son: {resultado}")
        self.assertEqual(resultado, ['D. Quijote de la Mancha'], ['EL INGENIOSO HIDALGO DON QUIJOTE DE LA MANCHA'])
    
    def test_palabras_unicas(self):
        resultado = palabras_unicas(r"C:\Users\Admin\eclipse-workspace\Dilior_Entregable\datosEntregable01\src\resources\archivo_palabras.txt")
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 8:")
        print(f"Las palabras únicas en el fichero archivo_palabras.txt son: {sorted(resultado)}")
        self.assertEqual(sorted(resultado), sorted(['proyecto', 'tecnologia', 'datos', 'programacion', 'software', 'ingenieria', 'futuro', 'codigo', 'python', 'salud']))

    def test_longitud_promedio_lineas(self):
        resultado = longitud_promedio_lineas(r"C:\Users\Admin\eclipse-workspace\Dilior_Entregable\datosEntregable01\src\resources\palabras_random.csv")
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 9:")
        print(f"La longitud promedio de las líneas del fichero palabras_random.csv es: {resultado}")
        self.assertAlmostEqual(resultado, 61.4, places=1)

        resultado_vacio = longitud_promedio_lineas(r"C:\Users\Admin\eclipse-workspace\Dilior_Entregable\datosEntregable01\src\resources\vacio.csv")
        print("\n############################################")
        print("TEST DE LA FUNCIÓN 9:")
        print(f"La longitud promedio de las líneas del fichero vacio.csv es: {resultado_vacio}")
        self.assertIsNone(resultado_vacio)

if __name__ == '__main__':
    unittest.main()

