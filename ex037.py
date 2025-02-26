num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases de conversão:')
print('[1] converter para BINARIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))

if opção == 1:
    print('O valor {} convertido em binario é {}'.format(num, bin(num)))
elif opção == 2:
    print('O valor {} convertido para octal é {}'.format(num, oct(num)))
elif opção == 3:
    print('O valor {} convertido para hexadecimal é {}'.format(num, hex(num)))
else:
    print('\033[0;31;40mOpção não encontrada. tente novamente.\033[m')