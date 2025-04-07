nums = []
num = 0
opção = ''

while True:
    i = 0
    num = int(input('Digite um valor: '))

    if num not in nums:
        nums.append(num)
        print('Valor adicionado')
    else:
        print('Número ja existente não sera adicionado.')
    opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if opção == 'N':
        break
print(f'Valores da lista {sorted(nums)}')
