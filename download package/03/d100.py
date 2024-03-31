from random import randint
from time import sleep
numeros = list()


def sorteia():
    print('Sorteando os valores da lista:', end=' ')
    for c in range(0, 5):
        a = randint(1, 10)
        print(a, end=' ')
        numeros.append(a)
        sleep(0.5)
    print('PRONTO!')
    sleep(0.5)

def somapar():
    soma = 0
    for d in numeros:
        if d % 2 == 0:
            soma += d
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
somapar()
