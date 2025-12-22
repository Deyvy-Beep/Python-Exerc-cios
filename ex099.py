def maior(* valores):
    from random import randint
    from time import sleep

    print('-='*21)
    sleep(0.5)
    print('Analisando valores informados...')
    for c in range(0, len(valores)):
        print(f'{valores[c]} ', end='', flush=True)
        sleep(0.5)
    print('Foram informados 6 valores ao todo.')
    sleep(1.5)
    print(f'O maior valor informado foi o {max(valores)}.')
    sleep(0.5)
    print('-=' * 20)

maior(4, 5, 2, 6, 9)
maior(2, 9, 3)
maior(0)
maior(2, 9, 3, 3, 7, 10)
