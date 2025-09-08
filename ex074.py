import random 

maior = int
menor = int
nums = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print('Os números gerados foram:', end=' ')
for c in range(0, len(nums)):
    print(nums[c], end=' ')

for c in range(0, len(nums)):
    if c == 0:
        maior = nums[c]
        menor = nums[c]
    elif nums[c] > maior:
        maior = nums[c]
    elif nums[c] < menor:
        menor = nums[c]
print(f'\nO maior número foi: {maior}')
print(f'O menor número foi: {menor}')
