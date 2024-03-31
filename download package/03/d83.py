expressao = input('Digite a expressão: ')
esquerdo = 0
direito = 0
for v in expressao:
    if v in '(':
        direito += 1
    if v in ')':
        esquerdo += 1
if direito == esquerdo:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')
