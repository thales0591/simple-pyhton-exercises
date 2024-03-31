dados = {}
dados['Nome'] = input('Nome: ')
dados['Média'] = float(input('Média: '))
if dados['Média'] >= 6:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}')
