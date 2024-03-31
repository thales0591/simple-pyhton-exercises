from random import choice
vc = input('Vamos jogar pedra, papel, ou tesoura! Vou escolher minha jogada, escreva a sua: ').strip()
ops = ['pedra', 'papel', 'tesoura']
pc = choice(ops)
vc = vc.lower()
if pc == vc:
    print(f'Haha! Eu também escolhi {vc}, empatamos!')
elif pc == 'pedra' and vc == 'papel':
    print(f'Que droga! Eu escolhi {pc}! \033[32mVocê venceu!\033[m')
elif pc == 'papel' and vc == 'pedra':
    print(f'Hahaha! Eu escolhi {pc}! \033[31mVocê perdeu!\033[m')
elif pc == 'tesoura' and vc == 'pedra':
    print(f'Que droga! Eu escolhi {pc}! \033[32mVocê venceu!\033[m')
elif pc == 'pedra' and vc == 'tesoura':
    print(f'Hahaha! Eu escolhi {pc}! \033[31mVocê perdeu!\033[m')
elif pc == 'tesoura' and vc == 'papel':
    print(f'Hahaha! Eu escolhi {pc}! \033[31mVocê perdeu!\033[m')
elif pc == 'papel' and vc == 'tesoura':
    print(f'Que droga! Eu escolhi {pc}! \033[32mVocê venceu!\033[m')
else:
    print('Ops! acho que você naão quer jogar pedra, papel ou tesoura hahaha.')
