def escreva(texto):
    tam = len(texto) + 4
    print('~'*tam)
    print(f'  {texto}')
    print('~'*tam)


msg = str(input('Digite a mensagem: '))
escreva(msg)
