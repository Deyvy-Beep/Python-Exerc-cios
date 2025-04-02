produtos = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Machila', 'Canetas', 'Livro')
preços = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for i in range(0, 9):
    print(f'{produtos[i]:.<30} R$ {preços[i]:>6}')
print('-'*40)