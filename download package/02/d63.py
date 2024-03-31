a = 0
b = 1
tot = 0
cont = 2
perg  = int(input('Digite quantos termos de fibonacci você quer: '))
if perg == 1:
    print('0 -', end=' ')
elif perg == 2:
    print('0 - 1 -', end=' ')
elif perg < 1:
    print('blz vacilao')
else:
    print('0 - 1 -', end=' ')
    while cont != perg:
        cont += 1
        tot = a + b
        print(tot, end=' - ')
        a = b
        b = tot
print('FIM')