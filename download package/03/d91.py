from random import randint
info = {}
infoorg = {}
for c in range(0, 4):
    info[f'jogador {c+1}'] = randint(1, 6)


def leitura(info):
    return info[1]


infoorg = sorted(info.items(), key=leitura, reverse=True)
print(infoorg)
print(info.keys())
