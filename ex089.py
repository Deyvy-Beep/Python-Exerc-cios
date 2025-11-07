from time import sleep
alunos = []
lista = []

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    lista.append((lista[1] + lista[2])/2)
    alunos.append(lista[:])
    lista.clear()
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if resp == 'N' or resp != 'S':
        break
print('-='*30)
print('N°  NOME      MÉDIA')
print('-'*24)
for c in range(0, len(alunos)):
    print(f'{c}   {alunos[c][0]}      {alunos[c][3]}')
print('-'*24)
while True:
    select = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if select == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    else:
        print(f'Notas de {alunos[select][0]} são {alunos[select][1:3]}')
        print('-'*24)
print('<<< VOLTE SEMPRE >>>')
