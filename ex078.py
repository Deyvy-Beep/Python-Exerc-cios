nums = []

for i in range(0, 5):
    nums.append(int(input(f'Digite o número da posição {i}: ')))
print(f'Os números foram {nums}')

print(f'O maior número foi {max(nums)} na posição ', end='')
for i, v in enumerate(nums):
    if v == max(nums):
        print(f'{i} ', end='')
print()

print(f'O menor número foi {min(nums)} na posição ', end='')
for i, v in enumerate(nums):
    if v == min(nums):
        print(f'{i} ', end='')
print()
