speed = int(input('Digite a velocidade do carro em km/h:'))
calc = (speed - 80) * 7
if speed <= 80:
    print('Ok! Tudo certo!')
else:
    print('Que pena! O carro ultrapassou o limite de velocidade e será multado em: R${}'.format(calc))
