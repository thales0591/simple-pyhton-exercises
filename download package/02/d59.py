n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0
maior = 0
print('''[1] somar
[2] multiplicar
[3] maior número
[4] novos números
[5] sair do programa''')
while op != 5:
    som = n1 + n2
    mult = n1 * n2
    op = int(input('Digite sua opção: '))
    maior = n1
    if op == 1:
        print(f'A soma entre os números é: {som}.')
    elif op == 2:
        print(f'A multiplicação entre eles é: {mult}.')
    elif op == 3:
        if maior < n2:
            maior = n2
            print(f'O maior número é {maior}.')
        else:
            print(f'O maior número é {maior}.')
    elif op == 4:
        n1 = int(input('Novo número 1: '))
        n2 = int(input('Novo número 2: '))
    else:
        print('Opcão inválida, tente novamente.')
