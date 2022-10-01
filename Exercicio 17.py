palavra = input('Digite uma palavra: ')
numero = int(input('Digite um número inteiro: '))

if len(palavra) > numero:
    nova_palavra = palavra[numero:] + palavra[:numero]
    print(nova_palavra)
else:
    print('Voce não digitou um número válido')