aluno = {'nome': str, 'media': float, 'situacao': str}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'A média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] <= 6 and aluno['media'] >= 4:
    aluno['situacao'] = 'Recuperação'
elif aluno['media'] < 4:
    aluno['situacao'] = 'Reprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
