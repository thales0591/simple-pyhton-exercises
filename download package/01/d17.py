cat1 = float(input('Cateto oposto:'))
cat2 = float(input('Cateto adjacente:'))
hip = (cat1 * cat1 + cat2 * cat2) ** (1/2)
print(f'O comprimento da hipotenusa é:{hip:.2f}')