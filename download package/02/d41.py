from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
calc = date.today().year - ano
print(f'O atleta tem {calc} anos.')
if calc <= 9:
    print('Classificação: MIRIM.')
elif 9 < calc <= 14:
    print('Classificação: INFANTIL.')
elif 14 < calc <= 19:
    print('Classificação: JUNIOR.')
elif 19 < calc <= 20:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')
