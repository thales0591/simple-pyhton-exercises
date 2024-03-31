from time import sleep


def a(b, co, d):
    if d < 0:
        d *= -1
    if d == 0:
        d += 1
    print('-=' * 20)
    print(f'Contagem de {b} até {co} de {d} em {d}')
    if b > co:
        ac = list(range(co, b+1, d))
        ac.sort(reverse=True)
        for ci in range(0, len(ac)):
            print(ac[ci], end=' ')
            sleep(0.5)
        print('FIM!')
    if co > b:
        aca = list(range(b, co+1, d))
        for cio in range(0, len(aca)):
            print(aca[cio], end=' ')
            sleep(0.5)
        print('FIM!')


a(1, 10, 1)
a(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
sas = int(input('Início: '))
sasb = int(input('Fim: '))
sasbc = int(input('Passo: '))
a(sas, sasb, sasbc)
