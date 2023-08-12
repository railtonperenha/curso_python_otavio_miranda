'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
# numero = input('Digite um número inteiro: ')

# try:
#     numero_inteiro = int(numero) # Converter String para Numero Inteiro
#     if (numero_inteiro % 2 == 0): # Resto da divisão igual a 0 para números pares
#         print(f'O número {numero_inteiro} é PAR!') # Caso seja número par, será exibido essa mensagem
#     else:
#         print(f'O número {numero_inteiro} é ÍMPAR!') # Caso seja ímpar, será exibido essa mensagem
# except:
#     print('Não foi inserido nenhum número inteiro!') # Caso não seja digitado nenhum número inteiro

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

horas = input('Que horas são agora: ')
try:
    horas = int(horas)
    if horas >= 0 and horas <= 11:
        print('Bom Dia!')
    elif horas >= 12 and horas <= 17:
        print('Boa Tarde!')
    elif horas >= 18 and horas <= 23:
        print('Boa Noite!')
    else:
        print('Desconheço esse horário!')
except:
    print('Digite apenas números inteiros!')

'''Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''

# nome = input('Digite seu nome: ')

# tamanho_nome = len(nome)

# if tamanho_nome > 1:
#     if tamanho_nome <= 4:
#         print('Seu nome é curto!')
#     elif tamanho_nome <= 6:
#         print('Seu nome é normal!')
#     elif tamanho_nome > 6:
#         print('Seu nome é muito grande!')
# else:
#     print('Digite um nome com mais de uma letra!')