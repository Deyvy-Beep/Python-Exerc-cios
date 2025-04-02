num = (int(input('Digite um número: ')), 
       int(input('Digite outro número: ')),
       int(input('Digite mias um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 aparece {num.count(9)} vezes')

if 3 in num == True:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição')
else:
    print('Nenhum número 3 encontrado na tupla')
print(f'Os valores pares digitados foram', end=' ')
for i in range(0, 4):
    if num[i] % 2 == 0:
        print(num[i], end=' ')
