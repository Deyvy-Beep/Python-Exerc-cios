valores = []

for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

    if c == 0:
        maior = menor = valores[c]
    elif maior < valores[c]:
        maior = valores[c]
        posi_Ma = c
    elif menor > valores[c]:
        menor = valores[c]
        posi_Men = c
    else:
        continue
print(valores)
print(f'O maior valor foi {maior} que esta na posição {posi_Ma}')
print(f'O menor valor foi {menor} que esta na posição {posi_Men}')
