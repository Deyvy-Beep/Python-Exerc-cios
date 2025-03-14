maior_p = 0
menor_p = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))

    if i == 1:
        maior_p = peso
        menor_p = peso
    elif peso > maior_p:
        maior_p = peso
    elif peso < menor_p:
        menor_p = peso
print(f'O maior peso lido foi de {maior_p}Kg')
print(f'O menor peso lido foi de {menor_p}Kg')
