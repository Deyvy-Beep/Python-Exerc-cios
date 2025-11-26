from random import randint
from time import sleep
from operator import itemgetter
n = 1
lista = list()
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = dict()
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-='*20)
print('== RANKING DE JOGADORES ==')
for p, v in enumerate(ranking):
    print(f' {p+1}° Lugar: {v[0]} com {v[1]}')
