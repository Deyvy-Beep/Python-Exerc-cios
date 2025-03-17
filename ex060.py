from math import factorial

num = int(input('Digite um número: '))

cont = 1
result = factorial(num)

print(f'Calculando {num}! = ', end='')
while cont < num:
    print(f'{cont} * ',end='')
    cont += 1
print(f'{num} = {result}')
