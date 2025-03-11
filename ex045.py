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

print('=-'*15)
print(f'O computador Jogou: {pc}')
print(f'O jogador jogou: {jogadas[jogador]}')
print('=-'*15)

if pc == 'Pedra' and jogador == 0:
    print('Deu empate')
if pc == 'Pedra' and jogador == 1:
    print('Jogador ganhou')
if pc == 'Pedra' and jogador == 2:
    print('Computador Ganhou')
if pc == 'Papel' and jogador == 0:
    print('Computador Ganhou')
if pc == 'Papel' and jogador == 1:
    print('Deu empate')
if pc == 'Papel' and jogador == 2:
    print('Jogador Ganhou')
if pc == 'Tesoura' and jogador == 0:
    print('Jogador Ganhou')
if pc == 'Tesoura' and jogador == 1:
    print('Computador Ganhou')
if pc == 'Tesoura' and jogador == 2:
    print('Deu empate')
