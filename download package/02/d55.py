maior = 0
menor = 0
for c in range(1, 6):
    n = int(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'o maior é {maior} e o menor é {menor}.')