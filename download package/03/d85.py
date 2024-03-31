lista = [[], []]
cop = []
for c in range(0, 7):
    a = int(input(f'Digite o {c+1}o. valor: '))
    if a % 2 == 0:
        lista[0].append(a)
    else:
        lista[1].append(a)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
