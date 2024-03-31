n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
calc = (n1 + n2) / 2
if calc < 5.0:
    print(f'REPROVADO. Sua média foi de {calc:.1f}.')
elif calc > 7:
    print(f'APROVADO. Sua média foi de {calc:.1f}.')
else:
    print(f'RECUPERAÇÃO. Sua média foi de {calc:.1f}.')
