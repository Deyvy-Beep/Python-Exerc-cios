jogador = dict()
dados = list()
jogos = 0
gols = list()
cont = 0
while True:
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for c in range(0, jogos):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    dados.append(jogador.copy())
    gols.clear()
    if resp not in 'SsNn':
        while True:
            resp = str(input('ERRO!! Responda com SIM ou NAO: ')).strip()[0]
            if resp in 'SsNn':
                break
    if resp in 'Nn':
        break
print('-='*30)
print(f'{'cod '} {'NOME':<15} {'GOLS':<15} {'TOTAL':<15}')
print('_'*40)
for c, v in enumerate(dados):
    print(f'{c:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('_'*40)
while True:
    opcao = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if opcao >= len(dados) and opcao != 999:
        print(f'ERRO! Não existe jogador {opcao}')
    elif opcao != 999:
        print(f'-- LEVANTAMENTO DO JOGADOR {dados[opcao]["Nome"]}')
        for c, v in enumerate(dados[opcao]["Gols"]):
            print(f'    No jogo {c+1} fez {v} gols')
    elif opcao == 999:
        break
print('>> VOLTE SEMPRE <<')
