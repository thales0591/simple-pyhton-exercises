dic = dict()
gols = list()
soma = 0
dic['nome'] = input('Nome do jogador: ')
npart = int(input(f'Quantas partidas {dic['nome']} jogou? '))
for c in range(0, npart):
    perg = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(perg)
    soma += perg
dic['gols'] = gols[:]
dic['total'] = soma
print('-='*30)
print(dic)
print('-='*30)
for pos, v in dic.items():
    print(f'O campo {pos} tem valor {v}.')
print('-='*30)
print(f'O jogador {dic['nome']} jogou {npart} partidas.')
for pos, v in enumerate(gols):
    print(f'    => Na partida {pos+1}, fez {v} gols.')
print(f'Foi um total de {soma} gols.')
