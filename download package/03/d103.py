def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


a = input('Nome do jogador: ')
b = input('Número de gols: ')
if b.isnumeric() and a.isalpha:
    if a.isnumeric():
        ficha(gols=int(b))
    else:
        if len(a.strip()) > 0 and len(b.strip()) > 0:
            ficha(a, int(b))
        if len(a.strip()) > 0 >= len(b.strip()):
            ficha(a)
        if len(b.strip()) > 0 >= len(a.strip()):
            ficha(gols=int(b))
        if len(a.strip()) <= len(b.strip()) <= 0:
            ficha()
else:
    if a.isnumeric():
        ficha()
    else:
        if len(a.strip()) == 0:
            ficha()
        else:
            ficha(a)
