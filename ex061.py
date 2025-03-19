print('=='*20)
print('Digite um número para descobrir a PA')
print('=='*20)

cont = 0

p_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

while cont < 10:
    print(f'{p_termo}', end=' → ')
    cont += 1
    p_termo += razão
print('Acabou')