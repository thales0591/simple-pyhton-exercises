from random import shuffle
n1 = input('Escolha 4 alunos e escreva o nome do primeiro:')
n2 = input('Do segundo:')
n3 = input('Do terceiro:')
n4 = input('Do quarto:')
deck = [n1, n2, n3, n4]
shu = shuffle(deck)
print(f'A sequência escolhida foi {deck}')
