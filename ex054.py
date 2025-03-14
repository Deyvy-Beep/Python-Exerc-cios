from datetime import date

ano_atual = date.today().year
datas = 0
menor = 0
maior = 0

for i in range(1, 8):
    datas = int(input(f'Qual o ano que a {i}ª pessoa nasceu: '))

    if ano_atual - datas < 18:
        menor += 1
    else: 
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
