#   2.1 - Números
print(1)
print(1.0)
print(1.)

# números por meio das funções embutidas
print(int(1.0))
print(int('9'))
print(float(1))
print(float('9.2'))
print(float('-inf'))
print(float('+inf'))
print(float('nan'))
print(complex(1,2))

# números e manipulações simples
print(3 + 2)
print(3 + 4.2)
print(4 / 2)
print(5 / 2)
print(5 // 2)
print(complex(1, 2) + 2)
print(complex(2, 0) + 0+1j)
print(2 + 0+1j)

'''
    Operadores aritméticos:
        x + y [adição]
        x - y [subtração]
        x / y [divisão em ponto flutuante]
        x // y [divisão descartando a parte fracionária]
        x * y [multiplicação]
        x % y [resto]
        -x [negação]
        x ** y [potência]
''' 
print(1 + 2)
print(3 - 1)
print(10 / 2)
print(10 // 3)
print(10 * 2 + 1)
print(10 % 3)
print(-3)
print(2 ** 8)

'''
    Operadores de bits
        x | y [ou]
        x ^ y [ou exclusivo]
        x & y [e]
        x << y [x com y bits deslocados à esquerda]
        x >> y [x com y bits deslocados à direita]
        ~x [inverso em bits]
'''
print(1 | 0)
print(1 | 5)
print(1 ^ 5)
print(4 & 1)
print(1 << 2)
print(4 >> 1)
print(~4)

#   2.3 - Criando e manipulando texto:String

st = 'macacana'
print(st[0])
print(st[1:4])
print(st[2:])
print(st[:3])
print(len(st))

'''
    x in y [se x está em y]
    x not in y [se x não está em y]
    x + t [concatenação de x com y]
    x * y [y repetições de x]
'''

print('m' in 'maracana')
print('x' not in 'maracana')
print('m' + 'aracana')
print('a' * 3)

# Principais métodos
print('maracana'.capitalize())
print('maracana'.count('a'))
print('maracana'.startswith('m'))
print('maracana'.endswith('z'))
print('copa de 2014'.split(' '))
print(''.join(['Copa', 'de', '2014']))
print('copa de 2014'.replace('2014', '2018'))

# Interpolação de string [% ou .format]
print('%d dias para copa' % 100)
print('{} dias para copa'.format(100))
print('{dias} dias para copa'.format(dias=100))

# configuração de espaçamento
print('|{:<60}|'.format('alinhado à esquerda, ocupando 60 posições'))
print('|{:>60}|'.format('alinhado à direita, ocupando 60 posições'))
print('|{:^60}|'.format('centralizado, ocupando 60 posições'))
print('|{:.^60}|'.format('centralizando ao alterar caracteres de espaçamento'))


