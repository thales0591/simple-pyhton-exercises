from datetime import date
ja = 0
nao = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    calc = date.today().year - nasc
    if calc >= 21:
        ja += 1
    else:
        nao += 1
print(f'{ja} pessoas JÁ atingiram a maioridade.')
print(f'{nao} pessoas ainda NÃO são maiores de idade.')