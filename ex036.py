P_casa = float(input('Qual o valor da casa que você deseja comprar: '))
salario = float(input('Qual o seu salário: '))
tempo_A = int(input('Em quantos ano você deseja pagar: '))

minimo = salario * (30/100)
tempo_M = tempo_A * 12
parcelas = P_casa / tempo_M

if parcelas > minimo:
    print('O valor das parcelas são de \033[0;31;40m R${:.2f} \033[m e vão ser pagas em {} meses\n\033[0;31;40m Emprestimo NEGADO\033[m'.format(parcelas, tempo_M))
else:
    print('O valor das parcelas são de \033[0;32;40m R${:.2f} \033[m e vão ser pagas em {} meses\n\033[0;32;40m Emprestimo APROVADO\033[m'.format(parcelas, tempo_M))

print('\nAnalise encerrada.')