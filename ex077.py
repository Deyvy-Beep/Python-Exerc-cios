palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in range(0, len(palavras)):
    print(f'\nA palavra {palavras[c]} tem as vogais: ', end='')
    palavra = palavras[c]
    for i in range(0, len(palavra)):
        if palavra[i] in 'AEIOU':
            print(palavra[i].lower(), end=' ')
