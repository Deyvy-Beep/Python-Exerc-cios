valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))

opção = 0

while opção != 5:
    print("""[1] Somar 
[2] Multiplicar 
[3] Maior 
[4] Novos números 
[5] Sair do programa""")
    opção = int(input('>>>Opção: '))
    if opção == 1:
        soma = valor1 + valor2
        print(f'\nA soma dos valores é: {soma}')
    elif opção == 2:
        mult = valor1 * valor2
        print(f'\nA multiplicação dos valores é: {mult}')
    elif opção == 3:
        if valor2 > valor1:
            print(f'\nO maior número é {valor2}')
        else:
            print(f'\nO maior número é {valor1}')
    elif opção == 4:
        valor1 = float(input('Digite um novo primeiro valor: '))
        valor2 = float(input('Digite um novo segundo valor: '))
print('Obrigado por usar nosso serviço!!')
