elemento = int(input('Informe o número que deseja procurar?'))        

def verificarElemento(elemento):
    tupla = (1,2,3,4,5,6,7,8,9,10)
    if elemento in tupla:
        print('O índice do elemento',elemento,'é:',tupla.index(elemento))
    else:
        print('O elemento não existe na Tupla.')
            
verificarElemento(elemento)