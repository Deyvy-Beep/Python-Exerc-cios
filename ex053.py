frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]    

print(f'A frase \n{junto}\nao contrario fica \n{inverso}')

if inverso == junto:
    print(f'\nA frase é um palíndromo')
else:
    print('\nA frase não é um palíndromo')
