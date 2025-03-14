nome = [""]*4
sexo = [""]*4
idade = [0]*4
Maior_N = ""
Maior_I = 0
cont = 0
Total_I = 0

for i in range(4):
    print(f'---- {i+1}ª pessoa ----')
    nome[i] = str(input('Nome: ')).strip()
    idade[i] = int(input('Idade: '))
    sexo[i] = str(input('Sexo [M/F]: ')).strip().upper()

    Total_I += idade[i]

    if idade[i] < 20 and sexo[i] == 'F':
        cont += 1
    if idade[i] > Maior_I and sexo[i] == 'M':
        Maior_I = idade[i]
        Maior_N = nome[i]
Idade_m = Total_I / 4

print(f'\nA média de idade do grupo é de {Idade_m:.1f} anos')
print(f'O homem mais velho tem {Maior_I} anos e se chama {Maior_N}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')
