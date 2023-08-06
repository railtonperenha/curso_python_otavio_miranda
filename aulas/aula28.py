'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
numero_str = input(
    'Digite um número e saiba o seu dobro: '
)
try:
    numero_float = float(numero_str)
    print(f'O dobro do {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número!')
