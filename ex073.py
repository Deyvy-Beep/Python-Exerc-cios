times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Bahia', 'Botafogo',
         'Mirassol', 'São Paulo', 'Bragantino', 'Fluminense', 'Ceará',
         'Corinthians', 'Atlético-MG', 'Internacional', 'Grêmio', 'Santos',
         'Vasco', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')

print('=-='*20)
print('Os 20 primeiros times do Campeonato Brasileiro de Futebol: \n')
for c in range(0, 20):
    if c % 5 == 0 and c != 0:
        print('')
    print(times[c], end=' - ')
print('')
print('=-='*20)
print(f'Os 5 primeiros colocados:\n\n{times[:5]}')
print('=-='*20)
print(f'Os últimos 4 colocados:\n\n{times[-4:]}')
print('=-='*20)
print(f'Organizado em ordem alfabetica:\n\n{sorted(times)}')
print('=-='*20)
print(f'Corinthians esta na {times.index('Corinthians')+1}ª posição')
print('=-='*20)
