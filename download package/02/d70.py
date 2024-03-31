tot = mil = pbarato = cont = 0
nbarato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço do produto: '))
    tot += preco
    cont += 1
    if cont == 1 or preco < pbarato:
        pbarato = preco
        nbarato = nome
    if preco > 1000:
        mil += 1
    perg = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while perg not in 'SsNn':
        perg = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if perg in 'Nn':
        break
print(f'R${tot} foi o total gasto.')
print(f'{mil} produtos custam mais de R$1000,00')
print(f'{nbarato.title()} é o nome do produto mais barato')
