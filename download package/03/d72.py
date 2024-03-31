ex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
      'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n > 20 or n < -20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    if -20 < n < 20:
        print(f'Você escolheu o número {ex[n]}')
        break
