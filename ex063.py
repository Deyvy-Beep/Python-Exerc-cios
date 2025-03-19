print('--'*20)
print('Sequência de Fibonacci')
print('--'*20)

num = int(input('Quantos termos você quer mostrar? '))

meio = 1
anterior = 0
proximo = 0
cont = 1

print(f'{anterior}', end=' → ')
while cont < num:
    print(f'{meio}', end=' → ')
    proximo = meio + anterior   
    anterior = meio
    meio = proximo
    cont += 1
print('FIM')
