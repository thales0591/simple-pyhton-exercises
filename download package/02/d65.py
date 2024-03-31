perg = ''
perg1 = int(input('Digite um número: '))
soma = 0
count = 1
maior = menor = perg1
while perg != 'N':
    perg = input('Deseja continuar? [S/N} : ').upper().strip()
    if perg == 'S':
        perg2 = int(input('Digite um número: '))
        soma += perg2
        count += 1
        if perg2 > maior:
            maior = perg2
        if perg2 < menor:
            menor = perg2
    if perg == 'N':
        print(f'Você digitou {count} números e a média foi {(soma + perg1) / count}')
        print(f'O maior valor foi {maior} e o menor foi {menor}')
