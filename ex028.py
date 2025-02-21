from random import randint
from time import sleep

print('=-='*20)
print('Vou pensar em número entre 0 e 5, tente adivinhar!')
print('=-='*20)

print('pensado...')
sleep(1)
num = randint(0, 5)

chute = int(input('Qual número eu pensei? '))

if chute > 5 or chute < 0:
    print('\nEu pensei em um número entre 0 e 5. Tente de novo.\n')
    breakpoint
else:
    if chute == num:
        print('=-='*20)
        print('\n Você acertou. PARABÉNS!! \n')
        print('=-='*20)
    else:
        print('=-='*20)
        print('\n O número foi {}. Eu ganhei!! \n'.format(num))
        print('=-='*20)
