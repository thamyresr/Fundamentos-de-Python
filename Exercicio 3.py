numero = int(input("Digite um número para que seja calculado o valor fatorial:"))
numero_fatorial = 1

for i in range(1, numero+1):
    numero_fatorial = numero_fatorial * i 

print('O número fatorial de', numero, 'é', numero_fatorial) 