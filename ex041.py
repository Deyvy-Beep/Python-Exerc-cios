from time import localtime

nasc = int(input('Ano de nascimento: '))

A_ano = localtime().tm_year
idade = A_ano - nasc


if idade <= 9:
    print(f'O atleta tem {idade} anos')
    print('Classificação: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos')
    print('Classificação: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anoss')
    print('Classificação: JUNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos')
    print('Classificação: SÊNIOR')
elif idade > 25:
    print(f'O atleta tem {idade} anos')
    print('Classificação: MASTER')
