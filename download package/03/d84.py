lista = []
sep = []
nomespes = []
nomeslev = []
maior = menor = 0
perg = ' '
while perg != 'N':
    sep.append(input('Digite o nome: '))
    sep.append(int(input('Digite o peso: ')))
    lista.append(sep[:])
    if len(lista) == 1:
        nomespes.append(lista[0][0])
        nomeslev.append(lista[0][0])
        maior = lista[0][1]
        menor = lista[0][1]
    sep.clear()
    perg = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while perg not in 'SsNn':
        perg = input('Quer continuar? [S/N]: ').strip().upper()[0]
for p in lista:
    if p[1] > maior:
        nomespes.clear()
        maior = p[1]
        nomespes.append(p[0])
    elif p[1] < menor:
        nomeslev.clear()
        menor = p[1]
        nomeslev.append(p[0])
    elif p[1] == maior:
        nomespes.append(p[0])
    elif p[1] == menor:
        nomeslev.append(p[0])
print(f'''{len(lista)} pessoas foram cadastradas.
{maior} foi o maior peso, de {nomespes}
{menor} foi o menor peso, de {nomeslev}''')
