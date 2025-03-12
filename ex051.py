print('='*20)
print('10 TERMOS DE UMA P.A')
print('='*20)

p_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

for i in range(1, 11):
    print(p_termo, end=' → ')
    p_termo += razão
print('Acabou')
