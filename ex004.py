algo = input('Digite algo: ')

print('\nO tipo primitivo desse valor é ', type(algo))

print('\nSo tem espaço?', algo.isspace())
print('\nÉ número?', algo.isnumeric())
print('\nÉ alfabético?', algo.isalpha())
print('\nÉ alfanumérico?', algo.isalnum())
print('\nEstá em maiúsculo?', algo.isupper())
print('\nEstá em minúsculo?', algo.islower())
print('\nEstá capitalizada?', algo.istitle())
print('\n')
