import random

n = soma = cont = 0
opção = ''

print('=-='*13)
print('Vamos joga PAR ou IMPAR')
print('=-='*13)

pc = random.randint(0, 10)

while True:
    n = int(input('Escolha um número: '))
    opção = str(input('Par ou Impar [P/I]: ')).strip().upper()

    soma = n + pc

    if soma % 2 == 0:
        print(f'A soma deu {soma} é PAR')

        if opção == 'P':
            print('Você ganhou!!')
            cont += 1
        else:
            print('Você perdeu!!')
            break
    else:
        print(f'A soma deu {soma} é IMPAR')

        if opção == 'I':
            print('Você ganhou!!')
            cont += 1
        else:
            print('Você perdeu!!')
            break
print(f'FIM DO JOGO!! Você ganhou um total de {cont} partidas.')
