from datetime import date
info = dict()
info['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
info['idade'] = date.today().year - nasc
info['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if info['ctps'] > 0:
    info['contratação'] = int(input('Ano de contratação: '))
    info['salário'] = float(input('Salário: R$ '))
    info['aposentadoria'] = (info['contratação'] + 35) - nasc
for pos, v in info.items():
    print(f'{pos} tem o valor {v}')
