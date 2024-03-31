print('Cadastro')
mais = 0
homens = 0
menos = 0
while True:
    idade = int(input('idade: '))
    sexo = input('sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = input('sexo [M/F]: ').strip().upper()[0]
    if idade > 18:
        mais += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        menos += 1
    perg = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while perg not in 'SsNn':
        perg = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if perg in 'Nn':
        break
print(f'{mais} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados.')
print(f'{menos} mulheres tem menos de 20 anos.')
