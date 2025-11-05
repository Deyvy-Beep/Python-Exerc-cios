from random import sample
from time import sleep
jogos = []
cont = 0

print('-'*25)
print('   JOGA NA MEGA SENA   ')
print('-'*25)

quant = int(input('Quantos jogos quer que eu gere: '))

print('-='*3, end='')
print(f' SORTEANDO {quant} JOGOS ', end='')
print('=-'*3)

while cont < quant:
    jogos.append(sample(range(1, 60), 6))
    cont += 1
for c in range(0, len(jogos)):
    jogos[c].sort()
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
print('-='*4, end='')
print(f' < BOA SORTE > ', end='')
print('=-'*4)
print('')
