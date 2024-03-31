distancia = float(input('Qual vai ser a distância da sua viagem em km?:'))
calc1 = distancia * 0.5
calc2 = distancia * 0.45
if distancia <= 200:
    print('Ok! Sua viagem é considerada curta e custará:R${:.2f}'.format(calc1))
else:
    print('Certo! sua viagem é considerada longa e custará:R${:.2f}'.format(calc2))
print('Boa viagem!')
