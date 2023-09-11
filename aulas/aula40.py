# Calculadora com while

while True:
    numero_1 = input('Primeiro Número: ')
    numero_2 = input('Segundo Número: ')
    operador = input('Escolha Operação: [+], [-], [/], [*]: ')

    numeros_validos = None
    
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Digite os números corretamente!')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Operador inválido!")
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue


    sair = input('Quer Sair ? [S] Sim: ').lower().startswith('s')

    if sair is True:
        break