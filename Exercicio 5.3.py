elemento = int(input('Informe o elemento de 1 a 10 para ser removida da tupla:'))

def eliminarElemento(elemento):
    tuplaInicial = (1,2,3,4,5,6,7,8, 9, 10)
    if elemento in tuplaInicial:
        elementoRemovido = elemento - 1
        tupla1 = tuplaInicial[0:elementoRemovido]
        tupla1 = tupla1 + tuplaInicial[elemento:]
        return print(tupla1)
    else:
        print('Elemento não existe dentro da tupla.')
eliminarElemento(elemento)
