red = '\033[0;31;40m'
green = '\033[0;32;40m'
close = '\033[m'

print('======== Iguaçu ========')

preço = float(input('Valor das compras: '))

print('FORMA DE PAGAMENTO')
print('[1] A vista dinheiro/cheque')
print('[2] Cartão de débito')
print('[3] Cartão de crédito')

opção = int(input('Qual a opção desejada: '))

if opção == 3:
    parcelas = int(input('Quantidade de parcelas (1 para não parcela): '))

    if parcelas < 5 and parcelas > 1:
        valor = (preço / parcelas)
        print(f'Valor das parcelas {green} R$ {valor:.2f} {close} em {parcelas} vezes sem juros ')
    elif parcelas >= 5:
        valor = (preço + (preço * 20/100)) / parcelas
        print(f'Valor das parcelas {green} R$ {valor:.2f} {close} em {parcelas} vezes com juros de 20%')
    elif parcelas == 1:
        print(f'Valor da compra ficou {green} R$ {preço:.2f} {close}')
elif opção == 2:
    valor = preço - (preço *(5/100))
    print(f'O valor ficou {green} R$ {valor} {close} com desconto de 5%')
elif opção == 1:
    valor = preço - (preço * (10/100))
    print(f'O valor ficou {green} R$ {valor} {close} com desconto de 10%')
else:
    print(f'{red} OPÇÃO INVALIDADE de pagamento. Tente Novamente! {close}')
