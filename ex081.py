nums = []
while True:
    nums.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar(S/N): ')).strip().upper()[0]
    if resp == 'S':
        continue
    elif resp == 'N':
        break
nums.sort(reverse=True)

print('-='*30)
print(f'Foram digitados o total de {len(nums)} valores')
print(f'Lista em ordem decrescente: {nums}')

if 5 in nums:
    print(f'O valor 5 apareceu {nums.count(5)} vezes')
else:
    print(f'Valor 5 não encontrado.')
print('-='*30)
