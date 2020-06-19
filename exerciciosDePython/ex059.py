'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar               [3] maior               [5] sair do programa
[2] multiplicar         [4] novos números
seu programa deverá realizar a operação solicitada em cada caso.'''
maior = 0
op = 0
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

while op != 5:
    print('''---------------------
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
---------------------''')

    op = int(input('>>>Digite a sua escolha: '))
    if op == 1:
        print('A soma dos valores {} e {} é {}'.format(num1,num2,(num1+num2)))
    elif op == 2:
        print('A multiplicação dos valores {} e {} é {}'.format(num1,num2,(num1 * num2)))
    elif op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior valor entre {} e {} é {}'.format(num1,num2,maior))
    elif op == 4:
        num1 = float(input('Digite um novo valor: '))
        num2 = float(input('Digite outro novo valor: '))
    elif op == 5:
        print('Saindo...')
    else:
        print('Digito invalido tente novamente!')
        op = int(input('>>>Digite a sua escolha: '))