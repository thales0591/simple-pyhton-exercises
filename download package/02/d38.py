n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
print('\033[34m:)\033[m')
