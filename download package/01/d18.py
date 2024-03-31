from math import cos,sin,tan,radians
ang = float(input('Me fale um ângulo:'))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)
print(f'Seu seno é {sen:.2f}, seu cosseno é {cos:.2f} e sua tangente vale {tan:.2f}')
