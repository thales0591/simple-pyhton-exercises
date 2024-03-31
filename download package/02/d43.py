peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}.')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está em sobrepreso.')
elif 30 <= imc < 40:
    print('Você está obeso.')
else:
    print('Você está em obesidade mórbida.')
