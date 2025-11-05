matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna = maior = 0
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor para [{c}][{i}]: '))
        if matriz[c][i] % 2 == 0:
            soma_par += matriz[c][i]
        if i == 2:
            soma_coluna += matriz[c][i]
        if c == 1:
            if i == 0:
                maior = matriz[c][i]
            elif matriz[c][i] > maior:
                maior = matriz[c][i]
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print('')
print('=-='*20)
print(f'Soma dos valores pares: {soma_par}')
print(f'Soma da terceira coluna: {soma_coluna}')
print(f'Maior valor da segunda linha: {maior}')
print('=-='*20)
