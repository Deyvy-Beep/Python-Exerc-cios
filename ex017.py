import math

C_oposto = float(input('Valor do cateto oposto: '))
C_adjacente = float(input('Valor do cateto adjacente: '))

hi = math.hypot(C_oposto, C_adjacente)

print('O valor da Hipotenusa: {:.2f}'.format(hi))
