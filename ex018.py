import math

ang = float(input('Digite um ang: '))

sen = math.sin(math.radians(ang))

print('O ang {} tem o seno de {:.2f}'.format(ang, sen))

cos = math.cos(math.radians(ang))

print('O ang {} tem o cosseno de {:.2f}'.format(ang, cos))

tang = math.tan(math.radians(ang))

print('O ang de {} tem a tangente de {:.2f}'.format(ang, tang))
