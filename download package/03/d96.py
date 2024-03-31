def area(n1, n2):
    conta = x * y
    print(f'A área de um terreno {n1:.1f}x{n2:.1f} é de {conta}m².')


print(f'{'Controle de terrenos':^25}')
print('-'*30)
x = float(input('Largura (m): '))
y = float(input('Comprimento (m): '))
area(x, y)
