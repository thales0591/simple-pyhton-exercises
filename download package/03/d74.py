from random import randint
tup = ()
tup2 = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
tup3 = tup + tup2
print(f'Os números gerados foram: {tup3}')
for c in range(0,5):
    if c == 0:
        maior = tup3[0]
        menor = tup3[0]
    else:
        if tup3[c] > maior:
            maior = tup3[c]
        if tup3[c] < menor:
            menor = tup3[c]
print(f'O maior valor é {maior}, e o menor é {menor}')
