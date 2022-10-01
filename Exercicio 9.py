import turtle

def desenharQuadrado():
    for i in range(4):
        for contador in range(4):
            turtle.right(90)
            turtle.bk(50)
        turtle.forward(50)

desenharQuadrado()

