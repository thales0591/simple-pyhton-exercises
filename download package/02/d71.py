valor = int(input('Que valor você quer sacar? '))
c50 = c20 = c10 = c1 = 0
while True:
    c50 = valor // 50
    if valor % 50 == 0:
        break
    valor -= (c50 * 50)
    c20 = valor // 20
    if valor % 20 == 0:
        break
    valor -= (c20 * 20)
    c10 = valor // 10
    if valor % 10 == 0:
        break
    valor -= (c10 * 10)
    c1 = valor // 1
    valor -= (c1 * 1)
    if valor == 0:
        break
print(f'Total de {c50} cédulas de R$50')
if c20 != 0:
    print(f'Total de {c20} cédulas de R$20')
if c10 != 0:
    print(f'Total de {c10} cédulas de R$10')
if c1 != 0:
    print(f'Total de {c1} cédulas de R$1')