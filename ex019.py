from random import choice

aluno1 = str(input('Nome do 1° aluno: '))
aluno2 = str(input('Nome do 2° aluno: '))
aluno3 = str(input('Nome do 3° aluno: '))
aluno4 = str(input('Nome do 4° aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]

sorte = choice(alunos)

print('O aluno escolhido foi {}'.format(sorte))
