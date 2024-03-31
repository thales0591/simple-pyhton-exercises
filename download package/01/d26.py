name = input('fala uma frase ai man:').strip()
up = name.upper()
print('A letra A aparece:', up.count('A'), 'vezes')
print('a primeira letra A aparece na posição:', int(up.find('A') + 1))
a = int(len(name))
b = int(up[::-1].find('A'))
c = a-b
print('o último A aparece na posição:', c)