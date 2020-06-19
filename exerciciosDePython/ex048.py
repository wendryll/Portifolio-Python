#Faça um programa que calcule a soma entre todos os números impares que são múltipls de três e que se encontram no intervalo de 1 até 500

soma = 0
n = 0
for i in range(1,501,2):
    if i % 3 == 0:
        n = n + 1
        soma = soma + i
print('A soma de todos os {} valores é {}'.format(n,soma))