'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A)Quantas vezes apareceu o valor 9                   C) Quais foram os números pares.
B) Em que posição foi digitado o primeiro valor 3'''

valor1 = int(input('Digite um valor inteiro: '))
valor2 = int(input('Digite outro valor: '))
valor3 = int(input('Digite mais um valor: '))
valor4 = int(input('Digite o ultimo valor: '))

numeros = (valor1,valor2,valor3,valor4)
quantNove = 0

print(numeros)

for i in range(len(numeros)):
    if numeros[i] == 9:
        quantNove += 1
print(f'O número 9 apareceu {quantNove} vezes')

for i in range(len(numeros)):
    if numeros[i] == 3:
        print(f'O valor 3 apareceu a primeira vez na {i+1}º posição')
        break

print('Os números digitados que são pares é: ', end='')
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=' ')
