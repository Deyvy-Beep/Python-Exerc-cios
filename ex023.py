num = int(input('Digite um número de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

if num <= 9999:
    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'Centena: {c}')
    print(f'Milhar: {m}')
else:
    print('Número deve ser entre 0 e 9999! Tente novamente')
