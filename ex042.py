lado1 = float(input('Valor do 1° lado: '))
lado2 = float(input('Valor do 2° lado: '))
lado3 = float(input('Valor do 3° lado: '))

red = '\033[0;31;40m'
green = '\033[0;32;40m'
close = '\033[m'

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print(f'Os lados {green} podem formar {close} um triangulo')
    
    if lado1 == lado2 == lado3:
        print(f'O triangulo é {green} EQUILÁTERO {close}')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print(f'O triangulo é {green} ISÓSCELES {close}')
    elif lado1 != lado2 != lado3 != lado1:
        print(f'O triangulo é {green} ESCALENO {close}')
else:
    print(f' {red} Os lados não podem formar um triangulo {close}')
