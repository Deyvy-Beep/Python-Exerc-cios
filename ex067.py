n = 0
cont = 1

while True:
    n = int(input('Digite um número: '))
    
    if n < 0:
        break
    else:
        print('-'*20)
        while cont <= 10:
            print(f'{n} x {cont} = {n*cont}')
            cont += 1
        print('-'*20)
        cont = 1
print('Fim')
