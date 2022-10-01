import turtle

def desenharQuadrado():
    lado = float(input('Entre com valor do lado do quadrado: '))
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
        
desenharQuadrado()