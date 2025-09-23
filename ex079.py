numeros = []
resp = ''
num = cont = 0
while True:
    num = int(input('Digite um número inteiro: '))
    if num in numeros:
        print('Valor ja existe e não sera adicionado!')
    else:
        numeros.append(num)
    resp = str(input('Deseja continuar?(S/N): ')).strip().upper()[0]
    if resp == 'S':
        continue
    elif resp == 'N':
        break
    else:
        print('Resposta não identificada! Interrompendo código!')
        break
numeros.sort()
print(f'A lista ordenada ficou: {numeros}')
