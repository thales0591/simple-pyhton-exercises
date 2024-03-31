frase = input('Digite uma frase: ').upper().strip()
sep = frase.split()
junt = ''.join(sep)
if junt == junt[::-1]:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')
print(junt, junt[::-1])