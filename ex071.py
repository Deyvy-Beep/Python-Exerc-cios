print('=='*15)
print('{:^30}'.format('Bem-Vindo ao Banco DEVY'))
print('=='*15)

saque = int(input('Quanto você deseja sacar: '))
cont50 = cont20 = cont10 = cont1 = 0
while True:
    while saque >= 50:
        saque -= 50
        cont50 += 1
    while saque >= 20:
        saque -= 20
        cont20 += 1
    while saque >= 10:
        saque -= 10
        cont10 += 1
    while saque >= 1:
        saque -= 1
        cont1 += 1
    if saque == 0:
        break
if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1')
