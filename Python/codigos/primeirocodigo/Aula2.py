a = int(input('Entre com o Primeiro Valor: '))
b = int(input('Entre com o Segundo valor: '))
print(type(a))
#a = #10
#b = #5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado  = ('Soma: {soma}. \nsubtracao: {subtracao}.'
       '\nMultiplicacao: {multiplicacao}'
    '\nDivicao: {divisao}'
       'Resto: {resto}'.format (soma=soma,
                                subtracao=subtracao,
                                resto=resto,
                                multiplicacao=multiplicacao,
                                divisao=divisao))
print(resultado)
