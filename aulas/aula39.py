# Iterando strings com while

nome = input('Nome: ')

tamanho_nome = len(nome)

indice = 0 #Primeira letra do nome
novo_nome = '' # Variável vázia para receber o nome após rodar o while por completo
while indice < len(nome): # Enquanto indice for menor que o nome [indice começando em 0]
    letra = nome[indice] # Variável que recebe as letras do nome digitado
    novo_nome += f'*{letra}' # Armazenar as letras do nome
    indice += 1
novo_nome += '*'
print(novo_nome)