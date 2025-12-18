def contador(inicio, fim, passo):
    from time import sleep
    print('-='*15)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    for c in range(inicio, fim+1, passo):
        sleep(0.1)
        print(f'{c} ', end='', flush=True)
    print("FIM!")
    print('-='*15)


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
