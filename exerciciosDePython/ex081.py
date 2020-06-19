'''Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
A) Quantos números foram digitados .
B) A lista de valores, ordenada de forma decrescente.
C) se o valor 5 foi digitado e está ou não na lista.'''
lista = []
cont = 0
num = 0

while True:
    lista.append(int(input('Digite um valor para acrescentar na lista: ')))
    cont += 1
    continuar = str(input('Deseja continuar[S/N]: '))[0].strip().upper()
    if continuar == 'N':
        break
print(f'A sua lista é:{lista}')
print(f'Foram digitados {cont} números.')
lista.sort(reverse=True)
print(f'A ordem decrescente da lista é {lista}')
for i in range(len(lista)):
    if lista[i] == 5:
        print('O número 5 foi digitado e está na lista.')