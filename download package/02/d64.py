soma = perg = 0
count = 0
perg = int(input('Digite um número [999 para parar]: '))
while perg != 999:
    soma += perg
    count += 1
    perg = int(input('Digite um número [999 para parar]: '))
print(f'Ao todo, você digitou {count} números.')
print(f'E a soma entre eles foi: {soma}.')
