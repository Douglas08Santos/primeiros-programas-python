#   3.2 - Pegando dados no terminal
salario = int(input('Salario? '))
imposto = float(input('Imposto em % [ex: 27.5]? '))
print('Valor real: {}'.format(salario - (salario * 
                                         imposto * 0.01)))

#   3.4 - Condicionais: IF, ELIF e ELSE
imposto2 = input('Imposto em % [ex: 27.5]? ')
if imposto2 == '':
    imposto2 = 27.5
else:
    imposto2 = float(imposto)
print('Valor real: {}'.format(salario - (salario * 
                                         imposto2 * 0.01)))
# Expressão if
imposto = 0.3
print('Alto' if imposto > 0.27 else 'Baixo')
imposto = 0.10
print('Alto' if imposto > 0.27 else 'Baixo')
valor_imposto = 'Alto' if imposto > 0.27 else 'Baixo'
print(valor_imposto)
