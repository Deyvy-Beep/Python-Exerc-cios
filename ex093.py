jogador = {'Nome': str, 'Gols': int, 'Total': int}
gols = list()
jogos = 0

jogador['Nome'] = str(input('Qual o nome do jogador: '))
jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))

for c in range(0, jogos):
    gols.append(int(input(f'   Quantos gols na partida {c}: ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas.')
for p, q in enumerate(gols):
    print(f'   => Na partida {p} fez {q} gols')
print(f'Foi um total de {jogador["Total"]} gols')
print('-='*30)
