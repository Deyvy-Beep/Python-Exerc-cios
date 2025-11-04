
matriz = [[], [], []]
cont = cont_princ = 0
while True:
    valor = int(input(f'Digite um valor para [{cont_princ}, {cont}]: '))
    matriz[cont_princ].append(valor)
    if cont_princ == 2 and cont == 2:
        break
    elif cont == 2:
        cont = 0
        cont_princ += 1
    else:
        cont += 1
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
