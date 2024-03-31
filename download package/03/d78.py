lista = []
maior = menor = cont = 0
for c in range(0, 5):
    lista.insert(c, int(input(f'Digite um valor para a posição {c}: ')))
b = lista[:]
posmaiores = []
posmenores = []
lista.sort()
for s, v in enumerate(b):
    if v == lista[4]:
        posmaiores.append(s)
    if v == lista[0]:
        posmenores.append(s)
print(f'A lista digitada foi: {b}')
print(f'O maior valor foi {lista[4]} nas posições:', end=' ')
for c in range(0, len(posmaiores)):
    print(posmaiores[c], end=' ')
print(f'\nO menor valor foi {lista[0]} nas posições:', end=' ')
for c in range(0, len(posmenores)):
    print(posmenores[c], end=' ')
