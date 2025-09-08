extenso = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove',
'dez', 'onze', 'doze', 'treze', 'catorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    
    while num < 0 or num > 20:
        num = int(input('Deve ser um valor entre 0 e 20. Tente novamente: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {extenso[num]}')
        resp = str(input('Deseja continuar?(S/N): ')).strip().upper()[0]
        if resp == 'S':
            continue
        else:
            break
print('Acabou!')
