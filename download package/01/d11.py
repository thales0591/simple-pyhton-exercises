info1 = float(input('Largura:'))
info2 = float(input('Altura'))
c1 = info1 * info2
c2 = c1 / 2
print('Se vc tem uma parede de medidas {:.2f}x{:.2f}, a área dela é de {:.2f}m² e tu vai precisar'.format(info1, info2, c1), end=' ')
print('de {:.2f} litros de tinta p pintar essa porra'.format(c2))