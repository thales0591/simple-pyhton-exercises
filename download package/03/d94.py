lista = list()
dic = dict()
perg = ' '
som = 0
while perg != 'N':
    dic['nome'] = input('Nome: ')
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    dic['sexo'] = sexo
    dic['idade'] = int(input('Idade: '))
    som += dic['idade']
    lista.append(dic.copy())
    dic.clear()
    perg = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    while perg not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        perg = input('Deseja continuar? [S/N]: ').upper().strip()[0]
media = som / len(lista)
print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {media} anos.')
print('- As mulheres cadastradas foram: ', end='')
for pos, v in enumerate(lista):
    if v['sexo'] == 'F':
        print(v['nome'], end=' ')
print('\nLista de pessoas que estão acima da média: ')
for pos, v in enumerate(lista):
    if v['idade'] > media:
        print(f'nome = {v['nome']}; sexo = {v['sexo']}; idade = {v['idade']};')
print('<< ENCERRADO >>')
