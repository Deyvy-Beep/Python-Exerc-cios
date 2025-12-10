pessoas = dict()
dados = list()
idade_media = 0.0
acima_media = list()
cont = 0
cont_M = list()
while True:
    pessoas["nome"] = str(input('nome: '))
    pessoas["idade"] = int(input('idade: '))
    pessoas["sexo"] = str(input('sexo: ')).strip().upper()[0]
    if pessoas['sexo'] not in "FfMm":
        while True:
            pessoas['sexo'] = str(input('Informação de sexo incorreta[F/M]: ')).strip().upper()[0]
            if pessoas['sexo'] in "FfMm":
                break
    if pessoas['sexo'] == 'F':
        cont_M.append(pessoas['nome'])
    dados.append(pessoas.copy())
    idade_media += pessoas['idade']
    resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    cont += 1
    if resp not in "NnSs":
        while True:
            resp = str(input('Responda S ou N: ')).strip().upper()[0]
            if resp in "NnSs":
                break
    if resp == 'N':
        break
    else:
        continue
idade_media = (idade_media/len(dados))
for c in range(len(dados)):
    if dados[c]['idade'] > idade_media:
        acima_media.append(dados[c])
print('-='*25)
print(f'A) Total de {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {idade_media}')
print(f'C) As mulheres cadastradas foram: ', end='')
print(', '.join(cont_M))
print(f'D) Lista de pessoas com idade acima da média:')
for c in range(len(acima_media)):
    print(f"    nome = {acima_media[c]["nome"]}; idade = {acima_media[c]["idade"]}; sexo = {acima_media[c]["sexo"]} ")
print('<< ENCERRADO >>')