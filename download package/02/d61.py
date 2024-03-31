pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
pa = pt
count = 0
while count != 10:
    print(pa, end=' ')
    pa += rz
    count += 1
