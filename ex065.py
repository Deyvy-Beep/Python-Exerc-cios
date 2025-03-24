opcao = 'S'
num = soma = maior = menor = cont = 0

while opcao in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num 
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
media = soma / cont

print(f'Você digitou {cont} números e a média foi de {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
