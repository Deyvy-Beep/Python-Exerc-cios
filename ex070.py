preço = soma = cont_MIL = menor = cont = 0
nome = nome_Menor = opção = ' '

print('--'*25)
print('      LOJA DO DEYVY      ')
print('--'*25)

while True:
    opção = ' '
    nome = str(input('Nome do produto: '))
    preço = int(input('Valor: R$ '))
    soma += preço
    cont += 1

    if preço > 1000:
        cont_MIL += 1
    if cont == 1 or preço < menor:
        nome_Menor = nome
        menor = preço
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if opção == 'N':
        break
print('--'*25)
print(f'Total gasto R$ {soma:.2f}')
print(f'Total de produtos acima de R$ 1.000: {cont_MIL}')
print(f'O produto mais barato foi {nome_Menor} com preço de R${menor:.2f}')
print('--'*25)
