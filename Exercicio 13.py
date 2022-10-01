from turtle import *

qtdQuadrado = int(input('Entre com o número de quadrados: ')) * 10
tamanho = int(input('Entre com o tamanho do primeiro quadrado: '))

def quadrado(posicaox,posicaoy,lado):
    penup()
    goto(posicaox,posicaoy)
    pendown()
    for contador in range(4):
        fd(lado)
        lt(90)
    
def desenharQuadrado(qtdQuadrado, tamanho):
    for contador in range(0, qtdQuadrado, 10):
        if tamanho <= 0:
            break
        else:
            tamanho -= 10
            quadrado(0 + contador/2, 0 + contador/ 2,tamanho)

desenharQuadrado(qtdQuadrado,tamanho)

