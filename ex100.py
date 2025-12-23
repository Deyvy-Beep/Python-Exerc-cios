def sorteia(lista):
    from random import randint
    from time import sleep

    print('Sorteando 5 valores da lista: ', end='', flush=True)
    sleep(0.4)
    for c in range(0, 5):
        lista.append(randint(0, 10))
        sleep(0.4)
        print(f"{lista[c]} ", end='', flush=True)
    print('PRONTO!')


def somaPar(lista):
    from time import sleep

    soma = 0
    print(f'Somando os pares de {valores}, temos ', end='', flush=True)
    sleep(1)
    for valor in valores:
        if valor % 2 == 0:
            soma += valor
        else:
            continue
    print(soma)


valores = list()
sorteia(valores)
somaPar(valores)
