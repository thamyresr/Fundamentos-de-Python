primeiroValor = float(input('Entre com o primeiro valor: '))
segundoValor = float(input('Entre com o segundo valor: '))
terceiroValor = float(input('Entre com o terceiro valor: '))
numero = (primeiroValor,segundoValor,terceiroValor)
if numero[0] + numero[1] > numero[2] and numero[1] + numero[2] > numero[0] and numero[0] + numero[2] > numero[1]:            
    if numero[0] == numero[1] and numero[0] == numero[2] and numero[1] == numero[2]:
        print('Este é um triângulo equilátero')    
    elif numero[0] == numero[2] or numero[0] == numero[1] or numero[1] == numero[2]:
        print('Este é um triângulo isósceles')
    else:
        print('Este é um triângulo escaleno')                            
else:
    print('Os valores não podem formar um triângulo')
