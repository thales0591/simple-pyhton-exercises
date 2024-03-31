def voto(x):
    idade = 0
    from datetime import date
    global idade
    idade = date.today().year - x
    if idade < 18:
        return 'VOTO NEGADO'
    if 60 > idade >= 18:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'


sit = voto(2005)
print(f'Com {idade} anos: {sit}')
