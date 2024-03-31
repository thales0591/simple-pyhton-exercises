listafoda = []
cop = []
cop2 = []
perg = perg2 = ' '
while perg != 'N':
    nome = input('Nome: ')
    cop.append(nome)
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2 : '))
    cop2.append(nota1)
    cop2.append(nota2)
    cop.append(cop2[:])
    cop.append((nota1 + nota2) / 2)
    listafoda.append(cop[:])
    cop.clear()
    cop2.clear()
    perg = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while perg not in 'SsNn':
        perg = input('Deseja continuar? [S/N]: ').strip().upper()[0]
print('-='*30)
print('No.  NOME        MÉDIA')
print('-'*30)
for c, v in enumerate(listafoda):
    print(f'{c:<4}{v[0]:<15}{v[2]:<5}')
print('-'*30)
while perg2 != 999:
    perg2 = int(input('Mostrar notas de qual aluno? (999 para interromper: '))
    for c, v in enumerate(listafoda):
        if c == perg2:
            print(f'As notas de {listafoda[c][0]} são: {listafoda[c][1]}')
print('Volte sempre!')
