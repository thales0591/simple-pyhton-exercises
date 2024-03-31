from time import sleep


def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    for c in range(0, len(num)):
        print(num[c], end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    maiorn = 0
    for d in range(0, len(num)):
        if d == 0:
            maiorn = num[d]
        else:
            if maiorn < num[d]:
                maiorn = num[d]
    print(f'O maior valor informado foi {maiorn}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
