matriz = []
cop = []
for d in range(0, 3):
    matriz.append(cop[:])
    for c in range(0, 3):
        a = int(input(f'Digite um valor para [{d}, {c}]: '))
        matriz[d].append(a)
for d in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[d][c]:^5}  ]', end=' ')
    print()
somadospares = 0
for v in matriz:
    for d in v:
        if d % 2 == 0:
            somadospares += d
maior = matriz[1][0]
for o in matriz:
    if o == matriz[1]:
        for comp in o:
            if comp > maior:
                maior = comp
print(f'A soma dos pares é: {somadospares}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é: {maior}')
