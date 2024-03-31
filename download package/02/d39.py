from datetime import date
nasc = int(input('Me informe seu ano de nascimento: '))
calc = date.today().year - nasc
rest = calc - 18
falt = 18 - calc
if calc < 18:
    print(f'Ufa! Você \033[32mainda vai\033[m se alistar no exército, e faltam {falt} anos.')
elif calc == 18:
    print('Cuidado! \033[33mEstá na hora\033[m de você se alistar no exército!')
else:
    print(f'Eita! \033[31mJá passou da hora\033[m de você se alistar no exército, já se passaram {rest} anos.')
