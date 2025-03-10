from random import choice
from time import sleep

jogadas = ['Pedra', 'Papel', 'Tesoura']
pc = choice(jogadas)

print('Suas opções: ')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

jogador = int(input('Qual a sua jogada? '))

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

if jogador == 0:
    jogador = 'Pedra'
elif jogador == 1:
    jogador = 'Papel'
elif jogador == 2:
    jogador = 'Tesoura'
else:
    print('Opção não reconhecida. Você perdeu!')

print(f'O computador Jogou: {pc}')
print(f'O jogador jogou: {jogador}')

if pc == 'Pedra' and jogador == 'Pedra':
    print('Deu empate')
if pc == 'Pedra' and jogador == 'Papel':
    print('Jogador ganhou')
if pc == 'Pedra' and jogador == 'Tesoura':
    print('Computador Ganhou')
if pc == 'Papel' and jogador == 'Pedra':
    print('Computador Ganhou')
if pc == 'Papel' and jogador == 'Papel':
    print('Deu empate')
if pc == 'Papel' and jogador == 'Tesoura':
    print('Jogador Ganhou')
if pc == 'Tesoura' and jogador == 'Pedra':
    print('Jogador Ganhou')
if pc == 'Tesoura' and jogador == 'Papel':
    print('Computador Ganhou')
if pc == 'Tesoura' and jogador == 'Tesoura':
    print('Deu empate')