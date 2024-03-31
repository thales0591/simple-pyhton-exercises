pre = float(input('Qual é o preço do produto? '))
cond = int(input('''-à vista: 1
-à vista no cartão: 2
-em até duas vezes no cartão: 3
-3x ou mais no cartão: 4
Qual a forma de pagamento? Digite uma dos números correspondentes acima: '''))
av = pre * 0.9
av_cart = pre * 0.95
duasvzs = pre
tresvzs = pre * 1.2
if cond == 1:
    print(f'O preço final foi de: R${av:.2f}.')
elif cond == 2:
    print(f'O preço final foi de: R${av_cart:.2f}.')
elif cond == 3:
    print(f'o preço final foi de: R${duasvzs:.2f}.')
elif cond == 4:
    print(f'O preço final foi de: R${tresvzs:.2f}.')
else:
    print('Ops! nenhuma das opções de pagamento foi selecionada :( ')
