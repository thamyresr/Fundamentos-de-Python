from turtle import* 
import math

def circulo():
    raio = float(input('Digite o valor do raio do círculo: '))
    circulo = raio * math.pi * 2
    circle(circulo)
    
circulo()

