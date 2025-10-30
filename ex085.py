nums = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}° valor: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
nums[0].sort()
nums[1].sort()
print('=-='*20)
print(f'Valores pares digitados: {nums[0]}')
print(f'Valores impares digitados: {nums[1]}')
print('=-='*20)
