'''
Created on 20 oct 2024

@author: Fonix
'''

import math

# 1. Producto (n - i + 1) para i de 0 a k
def producto_n_k(n, k):
    producto = 1
    for i in range(k + 1):
        producto *= (n - i + 1)
    return producto

# 2. Producto de los primeros k términos de una secuencia geométrica
def producto_geometrico(a1, r, k):
    producto = 1
    for i in range(k):
        producto *= a1 * r ** i
    return producto

# 3. Número combinatorio (n sobre k)
def combinatorio(n, k):
    return math.comb(n, k)

# 4. Cálculo de S(n, k) basado en la fórmula dada
def S_n_k(n, k):
    suma = 0
    for i in range(k):
        suma += ((-1) ** i) * (math.comb(k + 1, i + 1)) * ((k - i) ** n)
    return suma / math.factorial(k)

# 5. Método de Newton para encontrar x0
def metodo_newton(f, df, xn, epsilon):
    while abs(f(xn)) > epsilon:
        xn = xn - f(xn) / df(xn)
    return xn
