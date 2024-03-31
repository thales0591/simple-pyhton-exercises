from random import random, choice, randbytes, randint
nome1 = input('Escolha 4 nomes, digite o primeiro:')
nome2 = input('O segundo:')
nome3 = input('O terceiro:')
nome4 = input('O quarto:')
ran = choice([nome1, nome2, nome3, nome4])
print(f'O escolhido aleatoriamente é: {ran}')
