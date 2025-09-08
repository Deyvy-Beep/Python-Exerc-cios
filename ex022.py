from time import sleep

nome = str(input('Digite seu nome completo: ')).strip()

print('=-='*20)
print('Analisando seu nome...\n')
sleep(1)

print(f'{nome}')
print(f'Seu nome em maiúsculo é: {nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')
print(f'Seu nome tem o total de {len(nome.replace(" ", ""))} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e tem o total de {len(nome.split()[0])} letras')
