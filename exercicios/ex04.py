'''
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'seu nome INVERTIDO é {(nome[::-1])}')
    
    if ' ' in nome :
        print('Seu nome CONTÉM ESPAÇOS')
    else:
        print ('Seu nome NÃO CONTÉM ESPAÇOS')
    
    print(f'Seu nome CONTÉM {len(nome)} letras')
    print(f'A PRIMEIRA letra do seu nome é {nome[0]}')
    print(f'A ÚLTIMA letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vázios')