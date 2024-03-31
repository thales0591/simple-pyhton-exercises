year = int(input('Me fale um ano:'))
ycalc = year % 4
if ycalc == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')
