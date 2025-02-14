produto = float(input('Preço do produto: '))

desconto = produto*(5/100)
produtoN = produto-desconto

print('Seu produto ganhou 5% de desconto e ficou por R$ {:.2f}'.format(produtoN))