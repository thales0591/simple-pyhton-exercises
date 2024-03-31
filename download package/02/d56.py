soma = 0
velho = 0
m20 = 0
nvelho = ''
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: '.strip())
    soma += idade
    if sexo.upper() == 'M':
        if c == 1:
            velho = idade
            nvelho = nome
        else:
            if idade > velho:
                nvelho = nome
    else:
        if idade < 20:
            m20 += 1
media = soma / 4
print(f'''A média de idade do grupo é: {media}
O nome do homem mais velho é: {nvelho}
{m20} mulheres tem menos de 20 anos.''')
