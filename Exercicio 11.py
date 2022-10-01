from turtle import *

def desenharTriangulo():
    lado = float(input('Digite o valor do lado do triângulo: '))
    for i in range(3):
        fd(lado)
        lt(120)

desenharTriangulo()