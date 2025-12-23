def maior(* valores):
    from random import randint
    from time import sleep

    print('-='*21)
    sleep(0.5)
    print('Analisando valores informados...')
    for c in range(0, len(valores)):
        print(f'{valores[c]} ', end='', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo.')
    sleep(1.5)
    print(f'O maior valor informado foi o {max(valores)}.')
    sleep(0.5)
    print('-=' * 20)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
