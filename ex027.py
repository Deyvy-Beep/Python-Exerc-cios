nome = str(input('Digite seu nome completo: ')).strip().title().split()

print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome.pop()))
