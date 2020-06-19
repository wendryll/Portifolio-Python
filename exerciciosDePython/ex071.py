'''Crie um programa que simule o funcionamento de um caixa eletrônico.No início qual será o valor a ser sacado(número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs:Considere que o caixa possui células de R$50,R$20,R$10 e R$1'''

print('-'*40)
print('{:^40}'.format('Banco WSM'))
print('-'*40)

sacar = int(input('Qual o valor a sacar: R$'))
valor = sacar
cedula = 50
total = 0
while True:
    if valor >= cedula:
        valor -= cedula
        total += 1
    else:
        print(f'{total} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total = 0
        if valor == 0:
            break