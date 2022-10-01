numero = int(input("Digite um número para que seja calculado o valor fatorial:"))

contador = 1  
numeroFatorial = 1  
while contador <= numero:
    numeroFatorial = numeroFatorial * contador 
    contador = contador + 1
print('O numero fatorial de: ', numero, 'é', numeroFatorial)