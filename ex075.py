cont = 0
nums = (int(input('Digite um valor: ')), 
        int(input('Digite outro valor: ')), 
        int(input('Digite mais um valor: ')), 
        int(input('Digite o último valor: ')))
for c in range(0, len(nums)):
    if nums[c] % 2 == 0:
        cont += 1    
print(f'Os valores digitados foram: {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')
if 3 in nums:
    print(f'O valor 3 foi encontrar primeiramente na posição {nums.index(3)}')
else:
    print(f'O valor 3 não foi encontrado em nenhuma posição')
print(f'Tem o total de {cont} números pares')
