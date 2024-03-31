name = str(input('Qual é o seu nome completo?'))
print(f'tudo maiusculo:{name.upper()}')
print(f'tudo minusculo:{name.lower()}')
espacos = int(name.count(' '))
total = int(len(name))
print('O número de caracters exceto espaços é:', total-espacos)
nome1 = name.split()
a = nome1[0]
print('O numero de letras somente no primeiro nome é:', len(a))