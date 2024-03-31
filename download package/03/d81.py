perg = ' '
num = []
cont = 0
while perg != 'N':
    a = int(input('Digite um número: '))
    num.append(a)
    cont += 1
    perg = (input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while perg not in 'SsNn':
        perg = (input('Deseja continuar? [S/N]: ')).strip().upper()[0]
num.sort(reverse=True)
print(f'{cont} valores foram digitados.')
print(f'A lista de valores em ordem decrescente é: {num}')
if 5 in num:
    print('O valor 5 foi digitado e está na lista.')
else:
    print(f'O valor 5 não foi digitado e por isso não está na lista.')
