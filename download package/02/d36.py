casa = float(input('Digite o valor da casa:'))
money = float(input('Digite seu salário:'))
years = float(input('Digite em quantos anos você vai pagar:'))
mes = years * 12
prest = casa / mes
if prest > money * 0.3:
    print('\033[31mOops!\033[m Seu empréstimo foi \033[31mnegado.\033[m')
else:
    print('\033[32mParabéns!\033[m Seu empréstimo foi \033[32maprovado.\033[m')