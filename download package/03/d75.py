n = (int(input(f'Digite o valor 1: ')), int(input(f'Digite o valor 2: ')), int(input(f'Digite o valor 3: ')),
     int(input(f'Digite o valor 4: ')))
print(f'O número 9 apareceu {n.count(9)} vezes.')
if n.count(3) >= 1:
    print(f'O primeiro 3 apareceu na posição {n.index(3) + 1}.')
else:
    print('O 3 não foi digitado nenhuma vez.')
print('Os números pares foram: ', end=' ')
for c in range(0, 4):
    if n[c] % 2 == 0:
        print(n[c], end='  ')
