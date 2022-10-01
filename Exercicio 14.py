from turtle import *
import math

def quadrado():
    clear()
    for i in range(4):
        fd(100)
        lt(90)
        
def triangulo():
    clear()
    for i in range(3):
        fd(100)
        lt(120)

def circulo():
    clear()
    circulo = 2 * math.pi * 10
    circle(circulo)

listen()
onkey(quadrado, 'q')
onkey(triangulo, 't')
onkey(circulo, 'c')

