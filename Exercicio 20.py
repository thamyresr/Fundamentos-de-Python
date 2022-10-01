from turtle import *

linha = int(input('Digite um número inteiro: '))
angulo = int(input('Digite um ângulo: '))

def desenharComTartaruga(linha,angulo):
    shape('turtle')
    pencolor('red')
    for linha in range(0,linha):
        fd(linha)
        right(90 + angulo)
desenharComTartaruga(linha,angulo)