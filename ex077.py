nomes = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
         'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FURUTO')

for p in nomes:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end = ' ')
