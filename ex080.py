valores = []
valor = 0

for i in range(0, 5):

    valor = int(input('Digite um valor: '))

    if i == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao FIM da lista')
    else:
        j = 0
        for j in range(0, len(valores)):
            if valor <= valores[j]:
                valores.insert(j, valor)
                print(f'Valor adicionado na posição {j}')
                break
print(f'Lista: {valores}')
