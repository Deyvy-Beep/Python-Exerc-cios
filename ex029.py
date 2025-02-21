velocidade = float(input('Velocidde atingida: '))

acima = velocidade - 80
multa = acima * 7

if acima <= 0:
    print('Tudo certo, tenha um ótimo dia')

else:
    print('Você passou {:.2f}km acima do permitido. Multa de R${:.2f}'.format(acima, multa))
