num = []
perg = ' '
while perg != 'N':
    a = int(input('Digite um número: '))
    if a in num:
        print('Valor já existente, não vou adicionar')
    else:
        num.append(a)
        print('Ok, valor adicionado.')
    perg = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while perg not in 'SN':
        perg = input('Deseja continuar? [S/N]: ').strip().upper()[0]
num.sort()
print(f'Os valores digitados foram {num}')
