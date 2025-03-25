sexo = opção = ' '
idade = cont = cont_F = cont_M = 0

while True:
    sexo = opção = ' '
    print('CADASTRE UMA PESSOA')

    idade = int(input('Idade da pessoa: '))

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if idade > 18:
        cont += 1
    if sexo == 'M':
        cont_M += 1
    elif sexo == 'F' and idade < 20:
        cont_F += 1
    if opção in 'N':
        break
print(f'Total de pessoas maiores de 18 anos: {cont}')
print(f'Total de homens cadastrados: {cont_M}')
print(f'Total de mulheres menores de 20 anos: {cont_F}')
