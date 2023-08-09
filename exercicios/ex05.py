'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
numero = input(
    'Digite um número inteiro: '
)

try:
    numero_inteiro = int(numero) # Converter String para Numero Inteiro
    if (numero_inteiro % 2 == 0): # Resto da divisão igual a 0 para números pares
        print(f'O número {numero_inteiro} é PAR!') # Caso seja número par, será exibido essa mensagem
    else:
        print(f'O número {numero_inteiro} é ÍMPAR!') # Caso seja ímpar, será exibido essa mensagem
except:
    print('Não foi inserido nenhum número inteiro!') # Caso não seja digitado nenhum número inteiro

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

horas = input('Que horas são agora: ')
if int(horas) <= 11:
    print('Bom dia!')
elif int(horas) <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')

'''Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''

nome = input(
    'Digite seu nome: '
)

letras = len(nome) # Conta quantos caracteres tem seu nome
if letras <= 4:
    print('Seu nome é curto!')
elif letras <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')