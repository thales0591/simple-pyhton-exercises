n = int(input('Me diga um número:'))
perg = int(input('''-1 para binário
-2 para octal
-3 para hexadecimal
Agora me diga a base de conversão:'''))
if perg == 1:
    print(f'Seu número em binário é: {bin(n)[2:]}')
elif perg == 2:
    print(f'seu número em octal é: {oct(n)[2:]}')
elif perg == 3:
    print(f'seu número em hexadecimal é: {hex(n)[2:]}')
else:
    print('Ops! Você não nenhum dos números disponíveis!')
