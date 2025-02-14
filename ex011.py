alt = float(input('Qual a altura da parede em metros: '))
larg = float(input('Qual a largura da parede em metros: '))

area = alt * larg

tinta = area/2

print('A área da parede é de {}m² e você vai precisa de {}2.50L de tinta'.format(area, tinta))