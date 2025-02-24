lado1 = float(input('Valor do 1° lado: '))
lado2 = float(input('Valor do 2° lado: '))
lado3 = float(input('Valor do 3° lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('\033[0;32;40mOs segmentos podem formar um triângulo\033[m')
else:
    print('\033[0;31;40mOs segmentos não podem formar um triângulo\033[m')
