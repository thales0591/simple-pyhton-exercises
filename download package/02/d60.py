num = int(input('Digite um número: '))
fac = 0
c = 0
tot = 1
for c in range(1, num - 1):
    fac = num - c
    tot = tot * fac
print(num*tot)
