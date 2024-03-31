r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('terceiro segmento:'))
if r1 + r2 > r3 and r3 + r2 > r1 and r3 + r1 > r2:
    print('Parabéns! É possível formar um triângulo!')
else:
    print('Ops! Não é possível formar um triângulo :(')
