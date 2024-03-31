n1 = int(input('Escolha 3 números e digite o primeiro:'))
n2 = int(input('O segundo:'))
n3 = int(input('O terceiro:'))
if n1 >= n2 >= n3:
    print('o maior:', n1)
    print('o menor:', n3)
else:
    print()
if n2 >= n1 >= n3:
    print('o maior:', n2)
    print('o menor:', n3)
else:
    print()
if n1 >= n3 >= n2:
    print('o maior:', n1)
    print('o menor:', n2)
else:
    print()
if n2 >= n3 >= n1:
    print('o maior:', n2)
    print('o menor:', n1)
else:
    print()
if n3 >= n2 >= n1:
    print('o maior:', n3)
    print('o menor:', n1)
else:
    print()
if n3 >= n1 >= n2:
    print('o maior:', n3)
    print('o menor:', n2)
else:
    print()