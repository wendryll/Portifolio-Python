'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de 
uma sequencia de ficonacci.'''

n = int(input('Digite um número inteiro: '))
anterior = 0
proximo = 0
i = 0
while i < n:
    print(proximo,' -> ',end = '')
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo ==0:
        proximo += 1
    i += 1
print('FIM')

        