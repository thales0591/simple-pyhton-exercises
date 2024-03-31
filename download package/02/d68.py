from random import randint
print('Vamos jogar par ou impar!')
count = 0
while True:
    pc = randint(1, 2)
    n = int(input('Digite seu número: '))
    choice = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if choice in 'Ii' and (pc + n) % 2 == 0:
        print(f'Que pena! Eu escolhi {pc}, a soma deu {pc + n} que é par, eu ganhei!')
        break
    elif choice in 'Pp' and (pc + n) % 2 != 0:
        print(f'Que pena! Eu escolhi {pc}, a soma deu {pc + n} que é ímpar, eu ganhei!')
        break
    else:
        if choice in 'Pp':
            print(f'Você venceu! Eu escolhi {pc}, a soma deu {pc + n} que é par.')
            count += 1
        elif choice in 'Ii':
            print(f'Você venceu! Eu escolhi {pc}, a soma deu {pc + n} que é ímpar.')
            count += 1
        else:
            print('Ops! Digite novamente.')
print(f'Você realizou {count} vitórias consecutivas.')
