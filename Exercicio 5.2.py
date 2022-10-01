def retornarTuplas():
    tuplaInicial = (1,2,3,4,5,6)
    metade = int(len(tuplaInicial)/2)
    tupla1 = tuplaInicial[0:metade]
    tupla2 = tuplaInicial[metade:]
    return print('Tupla inicial: ', tuplaInicial,
                 '\nPrimeira metade da tupla inicial:', tupla1,
                 '\nSegunda metade da tupla inicial:', tupla2)    
retornarTuplas()