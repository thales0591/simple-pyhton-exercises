num = int(input('Digite um número: '))
dimi = 0
conta = 1
while dimi != num:
    dimi += 1
    conta = conta * dimi
print(f'O fatorial desse número é: {conta}.')