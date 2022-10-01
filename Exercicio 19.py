from turtle import*

quadrado = int(input('Digite um valor inteiro: '))

def desenharQuadrados(quadrado):
    shape('turtle')
    pencolor('red')
    for quadrado in range(0, quadrado):
        fd(quadrado)
        rt(90)

desenharQuadrados(quadrado)