distancia = float(input('Qual a distancia da sua viagem: '))

if distancia > 200:
    preço = distancia*0.45
    print('O preço da viagem é de R${:.2f} pela distancia de {:.1f}Km'.format(preço, distancia))
else:
    preço = distancia*0.50
    print('O preço da viagem é de R${:.2f} pela distancia de {:.1f}Km'.format(preço, distancia))
