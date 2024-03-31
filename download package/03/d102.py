def fatorial(n, show=False):
    cont = 1
    menos = 0
    f = n
    if show:
        while cont < n:
            f *= cont
            cont += 1
            print(f'{n-menos} x', end=' ')
            menos += 1
        print(f'1 = {f}')
    else:
        while cont < n:
            f *= cont
            cont += 1
        print(f)


fatorial(5)