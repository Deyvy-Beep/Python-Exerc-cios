from datetime import date

ano = int(input('\nQual ano deseja analisar? Digite 0 para usar ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto\n'.format(ano))

else:
    print('O ano {} não é bissexto\n'.format(ano))
