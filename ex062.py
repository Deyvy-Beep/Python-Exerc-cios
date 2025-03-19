print('=='*20)
print('Gerador de PA')
print('=='*20)

p_termo = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
cont = 0
v = 0
opção = 10

while opção != 0:
    while cont < opção:
        print(f'{p_termo}', end=' → ')
        p_termo += razão
        cont += 1
        v += 1
    print('PAUSA')
    cont = 0
    opção = int(input('Quantos termos você quer mostrar a mais? '))
print(f'\nProgressão finalizada com {v} termos mostrados')