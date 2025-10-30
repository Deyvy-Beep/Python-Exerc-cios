expr = str(input('Digite uma expressão: '))
pilha = []
pos = 0
for pos in expr:
    if pos == '(':
        pilha.append('(')
    elif pos == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
