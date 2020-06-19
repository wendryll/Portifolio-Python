'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar 
se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

ex = str(input('Digite uma expressão que use parênteses: '))
cont = 0
cont2 = 0

for i in range(len(ex)):
    if ex[i] == '(':
        cont += 1
    elif ex[i] == ')':
        cont2 += 1

if cont == cont2:
    print('A expressão está valida')
else:
    print('A expressão está invalida')