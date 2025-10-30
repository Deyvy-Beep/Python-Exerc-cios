pessoas = list()
dados = list()
pesados = list()
leves = list()
maior_p = 89.00
menor_p = 60.00
cont = p = 0

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    cont += 1
    if pessoas[cont-1][1] >= maior_p:
        pesados.append(dados[:])
    elif pessoas[cont-1][1] <= menor_p:
        leves.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    else:
        continue
print('=-'*19)
print(f'Total de pessoas cadastradas: {cont}')
for p in pesados:
    print(f'{p[0]} com {p[1]}kg (Considerado/a pesado)')
for p in leves:
    print(f'{p[0]} com {p[1]}kg (Considerado/a leve)')
print('=-'*19)
