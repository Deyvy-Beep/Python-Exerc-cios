nums = []
nums_Impares = []
nums_Pares = []
while True:
    nums.append(int(input('Digite um valor: ')))
    if nums[-1] % 2 == 0:
        nums_Pares.append(nums[-1])
    else:
        nums_Impares.append(nums[-1])
    resp = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
    elif resp == 'S':
        continue
nums.sort(reverse=True)
nums_Pares.sort(reverse=True)
nums_Impares.sort(reverse=True)
print('-='*30)
print(f'Lista com todos os valores: {nums}')
print(f'Lista com valores pares: {nums_Pares}')
print(f'Lista com valores impares: {nums_Impares}')
print('-='*30)
