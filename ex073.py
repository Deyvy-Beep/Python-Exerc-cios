times = ('Cruzeiro', 'Atlético-MG', 'Sport', 'Flamengo', 'Internacional',
         'RedBull Bragantino', 'Vasco', 'Ceará', 'Corinthians', 'Bahia',
         'Grêmio', 'São Paulo', 'Botafogo', 'Fluminense', 'Santos',
         'Fortaleza', 'Juventude', 'Palmeiras', 'Mirassol', 'Vitória')
print('-='*30)
print(f'Lista de times do brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros são {times[:5]}')
print('-='*30)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*30)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O Sport esta na {times.index("Sport")+1}° posição')
print('-='*30)
