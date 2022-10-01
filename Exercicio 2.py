anos = int(input('Digite quantos anos você tem: '))
meses = int(input('Digite quantos meses se passaram desde o seu último aniversário:'))
dias = int(input('Digite a diferença entre o dia do seu aniversário e a data atual: '))

diasAno = 365
diasMes = 30

totalDias = (anos * diasAno) + (meses * diasMes) + dias

print('Total de dias:',totalDias)