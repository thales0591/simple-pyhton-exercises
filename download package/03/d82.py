num = []
pares = []
impares = []
perg = ' '
while perg != 'N':
    a = int(input('Digite um número: '))
    num.append(a)
    perg = (input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while perg not in 'SsNn':
        perg = (input('Deseja continuar? [S/N]: ')).strip().upper()[0]
for v in num:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista principal é: {num}')
print(f'A lista somente dos pares é: {pares}')
print(f'A lista somente dos ímpares é: {impares}')
