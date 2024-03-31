times = ('palmeiras', 'gremio', 'ateltico-mg', 'flamengo', 'botafogo', 'bragantino', 'fluminense',
         'athtletico-pr', 'internacional', 'fortaleza', 'sao paulo', 'cuiaba', 'corinthians', 'cruzeiro',
         'vasco', 'bahia', 'santos', 'goias', 'coritiba', 'america-mg')
print(f'Os cinco primeiros colocados são: ', end='')
for c in range(0, 5):
    print(times[c], end=' ')
print(f'\nOs quatro últimos colocados são: ', end='')
for d in range(-4, 0):
    print(times[d], end=' ')
print(f'''\nOs times em ordem alfabética:
{sorted(times)}''')
a = times.index('bahia')
print(f'O time do bahia se encontra na posição {a+1}')
