from turtle import *

color("Purple")
pensize(3)

passos = 100
anguloTotal = 360
contador = 0

write(contador)
backward(passos)

for contador in range(15, anguloTotal, 15):
    setheading(contador)
    forward(passos)
    write(contador)
    backward(passos)
    
done()