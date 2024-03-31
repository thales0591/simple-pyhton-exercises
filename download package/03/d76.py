tupla = ('lapis', 3, 'borracha', 5, 'esquadro', 12, 'notebook', 120, 'mochila', 50)
print('-'*40)
print(f'{' LISTAGEM DE PREÇOS ':^40}')
print('-'*40)
for c in range(0, len(tupla), 2):
    a = '.' * (30 - len(tupla[c]))
    print(f'{tupla[c]}{a}R$ {tupla[c+1]:>7.2f}')
print('-'*40)
