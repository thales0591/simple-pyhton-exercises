num = int(input('Digite um número: '))
s = 0
n = 0
for c in range(1, 500):
    if num % c == 0:
        s = s + 1
    elif num % 1 == 0 and num % num == 0:
        n = n + 1
if s > 2:
    print('Não é primo')
else:
    print('É primo.')