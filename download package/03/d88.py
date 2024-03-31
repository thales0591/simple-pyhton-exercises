from random import randint
from time import sleep
megasena = []
cop = []
print('-'*40)
print(f'{'MEGA SENA':^40}')
print('-'*40)
perg = int(input('Quantos jogos serão gerados?: '))
for c in range(0, perg):
    megasena.append(cop[:])
    while True:
        a = randint(0, 60)
        if a not in megasena[0]:
            megasena[c].append(a)
        if len(megasena[c]) == 6:
            break
    megasena[c].sort()
print(f'{f'SORTEANDO {perg} JOGOS...':^40}')
sleep(1)
for c in range(0, len(megasena)):
    print(f'Jogo {c+1}: {megasena[c]}')
    sleep(1)
print(f'{' BOA SORTE! ':-^40}')