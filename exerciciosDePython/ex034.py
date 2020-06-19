#escreva um programa que pergumte o sálario de um funcionário e calcule o valor do deu aumento.Para salários superiores a R$1.250,00, calcule um aumento de 10% para os inferiores ou iguair, o aumento é de 15%.

salario = float(input('Digite o valor do salário do funcionario: R$'))
if salario <= 1250:
    print('O funcionario que recebe R${} passa a ganhar R${}'.format(salario,salario + salario * 0.15))
else:
    print('O funcionario que recebe R${} passa a ganhar R${}'.format(salario,salario + salario * 0.10))