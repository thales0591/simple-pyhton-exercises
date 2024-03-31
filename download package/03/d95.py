lista = list()
dic = dict()
gols = list()
soma = perg2 = 0
perg = npart = ' '
while perg != 'N':
    dic['nome'] = input('Nome do jogador: ')
    npart = int(input(f'Quantas partidas {dic['nome']} jogou? '))
    for c in range(0, npart):
        perg = int(input(f'Quantos gols na partida {c+1}? '))
        gols.append(perg)
        soma += perg
    dic['gols'] = gols[:]
    dic['total'] = soma
    lista.append(dic.copy())
    gols.clear()
    dic.clear()
    soma = 0
    perg = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while perg not in 'SsNn':
        print('Erro! Responda apenas S ou N.')
        perg = input('Quer continuar? [S/N]: ').strip().upper()[0]
print('-='*25)
print(f'{'Cód.':<6}{'Nome':<14}{'Gols':<10}{'Total':>10}')
print('-'*45)
for pos, v in enumerate(lista):
    print(f'{pos:<4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*45)
while perg2 != 999:
    perg2 = int(input('Mostrar dados de qual jogador?(999 para parar) '))
    if perg2 >= len(lista) or perg2 < 0:
        print(f'Ops! Não existe jogador com o código {perg2}! Tente novamente.')
    else:
        for pos, v in enumerate(lista):
            if pos == perg2:
                print(f'{f'LEVANTAMENTO DO JOGADOR {v['nome']}':^35}')
                for pos1, v1 in v.items():
                    if v1 == v['gols']:
                        for c in range(0, len(v['gols'])):
                            print(f'{f'No jogo {c+1} fez {v1[c]} gols.':^35}')
print(' << VOLTE SEMPRE >>')
