#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do salário R$'))
aumento = float(input('Digite a porcentagem de aumento: '))
novoSalario = salario + (salario * aumento/100)
print('O salário depois do aumento será {:.2f}'.format(novoSalario))