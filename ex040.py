nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

green = '\033[0;32;40m'
red = '\033[0;31;40m'
close = '\033[m'

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Aluno {green}APROVADO{close} com média {media:.1f}')
elif media >= 5 and media <= 6.9:
    print(f'O aluno esta de {red}RECUPERAÇÃO{close} com média {media:.1f}')
elif media < 5:
    print(f'O aluno esta {red}REPROVADO{close} com média {media:.1f}')
