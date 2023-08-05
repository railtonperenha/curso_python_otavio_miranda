'''
Formatação básica de strings
s - string
d - int
f - float
(Caractere)(><^)(quantidade)
Sinal - + ou -
Ex.: 0>-100,.1f
'''

variavel = 'ABC'
print(f'{variavel}')

# > - Esquerda
print(f'{variavel: >10}')

# < - Direita
print(f'{variavel: <10}.')

# ^ - Centro
print(f'{variavel: ^10}.')

# . <número de digitos>
print(f'{1000.4873648123746:,.1f}')

# = - Força o número aparecer antes dos zeros
print(f'{1000.4873648123746:0=+10,.1f}')

# x ou X - Hexadecimal
print(f'O hexadecimal de {1500} é {1500:08x}')

# Conversion flags - !r !s !a
print(f'{variavel!r}')