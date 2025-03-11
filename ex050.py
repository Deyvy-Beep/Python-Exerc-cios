soma = 0
cont = 0

for i in range(0, 6):
    num = int(input('digite um número inteiro: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f'A soma dos {cont} números pares que você informou é {soma}')
