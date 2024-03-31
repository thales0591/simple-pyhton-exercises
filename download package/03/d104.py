def leiaint(num):
    a = input(num)
    while not a.isnumeric():
        print('Erro! Digite um número inteiro válido.')
        a = input(num)
    return a


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
