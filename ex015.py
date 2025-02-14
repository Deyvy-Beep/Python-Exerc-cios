km = float(input('Quantos quilometros você rodou com o carro: '))
dias = int(input('Quantos dias você ficou com o carro: '))

Total = (dias * 60) + (km * 0.15)

print('Total a pagar pelo aluguel e uso do carro: R$ {:.2f}'.format(Total))
