num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases de conversão:')
print('[1] converter para BINARIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))

if opção == 1:
    print('O valor {} convertido em binario é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O valor {} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O valor {} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('\033[0;31;40mOpção inválida. tente novamente.\033[m')
