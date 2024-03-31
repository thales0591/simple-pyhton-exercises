n1 = float(input('Lado 1: '))
n2 = float(input('Lado 2: '))
n3 = float(input('Lado 3: '))
if n1 + n2 > n3 and n3 + n2 > n1 and n1 + n3 > n2 and n1 == n2 and n1 != n3:
    print('Seu triângulo é isósceles.')
elif n1 + n2 > n3 and n3 + n2 > n1 and n1 + n3 > n2 and n1 == n3 and n2 != n1:
    print('Seu triângulo é isósceles.')
elif n1 + n2 > n3 and n3 + n2 > n1 and n1 + n3 > n2 and n2 == n3 and n2 != n1:
    print('Seu triângulo é isósceles.')
elif n1 + n2 > n3 and n3 + n2 > n1 and n1 + n3 > n2 and n1 == n2 == n3:
    print('Seu triângulo é equilátero.')
elif n1 + n2 > n3 and n3 + n2 > n1 and n1 + n3 > n2 and n1 != n2  and n2 != n3 and n3 != n1:
    print('Seu triângulo é escaleno.')
else:
    print('Não é possível formar um triângulo com esses lados.')
