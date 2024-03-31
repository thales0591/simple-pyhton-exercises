name = input('Fale uma cidade:').strip()
corte = name.split()
print('O nome da cidade começa com santo?')
print('SANTO' in corte[0].upper())