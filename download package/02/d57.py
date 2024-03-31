sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Por favor, digite novamente.')
print('Ok, aceito.')
