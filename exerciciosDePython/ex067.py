'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('-'*20)
    print('Tabuada')
    print('-'*20) 
    num = int(input('Digite um número inteiro para ver sua tabuada: '))
    if num > 0:
        for i in range(1,11):
            print(f'{num} x {i} = {num*i}')
    else:
        print('Saindo...')
        break
print('Volte sempre!')
