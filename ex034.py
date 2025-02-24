salario = float(input('Digite seu salário: '))

if salario > 1250:
    N_salario = salario + (salario * (10/100))
else:
    N_salario = salario + (salario * (15/100))

print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(salario, N_salario))