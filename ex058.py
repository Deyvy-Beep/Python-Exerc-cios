from random import randint
from time import sleep

print('Tente adivinhar o número entre 0 e 10')
print('Pensando...')
sleep(1)
num = randint(0, 10)
cont = 0
print('Acabei de pensar em um número\n')

palpite = int(input('Qual o seu palpite? '))

while palpite != num:
    if palpite > num:
        palpite = int(input('Valor pensado é menor: '))
    elif palpite < num:
        palpite = int(input('Valor pensado é maior: '))
    cont += 1
if cont > 0:
    print(f'\nO número era {num}. Parabéns você acertou com {cont} tentavidas!!')        
else:
    print(f'O número era {num}. Parabéns você acertou de primeira!!')
