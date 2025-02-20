from time import sleep

nome = str(input('Digite seu nome completo: ')).strip()

print('=-='*20)
print('Analisando seu nome...\n')
sleep(1)

print('Seu nome em maiúsculo é', nome.upper())
print('Seu nome em minúsculo é', nome.lower())

print('Seu nome tem {} letras'.format(len(nome.replace(" ", ""))))

N_nome = nome.split()

print('Seu primeiro nome é {} e ele tem {} letras'.format(N_nome[0], len(N_nome[0])))

print('=-='*20)
