nome = 'Railton'
altura = 1.79
peso = 80
imc = peso / altura ** 2

#f-strings
linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso:.2f} e se IMC é'
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)

# Railton tem 1.80 de altura,
# pesa 80kg e seu IMC é
# de 20.00