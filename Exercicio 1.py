numeroImpar = int(input('Digite um número impar:'))
soma = 0

if numeroImpar % 2 != 0:
    for contador in range(numeroImpar + 1):
        if contador % 2 != 0:
            soma = soma + contador
    print(soma)
else:
    print('O número digitado não é um número impar.')
    
    