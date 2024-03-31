from time import sleep


def doidera(perg=''):
    b = f"  SISTEMA DE AJUDA PyHelp"
    print('\033[32m~' * (len(b) + 2))
    print(b)
    print(f"{'~' * (len(b) + 2)}\033[m", flush=True)
    while perg != 'fim':
        perg = input('Função ou Biblioteca > ').lower().strip()
        if perg == 'fim':
            break
        sleep(0.5)
        a = f"  Acessando o manual do comando '{perg}'"
        print('\033[0;34m~'*(len(a) + 2))
        print(a)
        print(f"{'~' * (len(a) + 2)}\033[m", flush=True)
        sleep(2)
        print('\033[7m', end='')
        help(perg)
        print(f'\033[m')
    print('Até logo!')


doidera()
