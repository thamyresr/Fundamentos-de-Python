import turtle
import math

def desenharPoligono(tartaruga, n, r):
    desenharPoligono1(tartaruga, n, r)
    tartaruga.pu()
    tartaruga.fd(r*2 + 10)
    tartaruga.pd()
    
def desenharPoligono1(tartaruga, n, r):
    angulo = 360.0 / n
    for i in range(n):
        desenharPoligono2(tartaruga, r, angulo/2)
        tartaruga.lt(angulo)

def desenharPoligono2(tartaruga, r, angulo):
    y = r * math.sin(angulo * math.pi / 180)

    tartaruga.rt(angulo)
    tartaruga.fd(r)
    tartaruga.lt(90+angulo)
    tartaruga.fd(2*y)
    tartaruga.lt(90+angulo)
    tartaruga.fd(r)
    tartaruga.lt(180-angulo)

bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

size = 40
tam = int(input('Informe o número de segmentos: '))
desenharPoligono(bob, tam, size)