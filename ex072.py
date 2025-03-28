numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quarto',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = cont = 0
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente Novamente.', end=' ')
    else:
        cont += 1
        print(f'Você digitou o número {numeros[num]}')
        opção = str(input('Você quer continuar?[S/N]: ')).strip().upper()[0]
        if opção == 'N':
            break
print(f'Você digitou {cont} números')
