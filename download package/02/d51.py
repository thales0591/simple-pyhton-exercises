pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
ultimac = pt + (10 - 1) * rz
for c in range (1, 10):
    print(pt + (c - 1) * rz, end= ' → ')
print(f'{ultimac} → ACABOU')