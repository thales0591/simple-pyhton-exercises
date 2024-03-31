salario = float(input('Digite seu salário:'))
if salario >= 1250.00:
    print('Seu novo salário é de:R${:.2f}'.format(salario * 1.1))
else:
    print('Seu novo salário é de:R${:.2f}'.format(salario * 1.15))