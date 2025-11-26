from datetime import datetime
ano_atual = datetime.now().year
pessoa = {'Nome': str, 'Idade': int, 'CTPS': int}
pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = ano_atual - int(input('Data de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - ano_atual)
    print('-='*25)
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
else:
    print('-='*25)
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
