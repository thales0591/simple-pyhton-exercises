from random import randint
number = randint(0, 10)
suggest = ''
nt = 1
while number != suggest:
    suggest = int(input('Tente advinhar um número de 0 a 10: '))
    if suggest == number:
        print('Parabéns, você acertou!')
    else:
        print('Errou!')
        nt += 1
print(f'Foram necessárias {nt} tentativas até você acertar.')