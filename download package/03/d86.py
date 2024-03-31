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
