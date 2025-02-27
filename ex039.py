from time import localtime

A_ano = localtime().tm_year

nasc = int(input('Qual ano você nasceu: '))

idade = A_ano - nasc

if idade == 18:
    print(f'Quem nasceu em {nasc} tem {idade} anos em {A_ano}')
    print('Deve se alistar IMEDIATAMENTE!!')
elif idade > 18:
    saldo = idade - 18
    print(f'Quem nasceu em {nasc} tem {idade} anos em {A_ano}')
    print(f'Ja deveria ter se alistado há {saldo} anos')
    print(f'Seu alistamento deveria ter sido em {A_ano - saldo}')
else:
    saldo = 18 - idade
    print(f'Quem nasceu em {nasc} tem {idade} anos em {A_ano}')
    print(f'Ainda falta {saldo} anos para se alistar')
    print(f'Seu alistamento sera em {A_ano + saldo}')
