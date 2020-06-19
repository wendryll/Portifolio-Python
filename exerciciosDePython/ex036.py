#Escreva um programa para aprovar o empréstimo bancário para. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Em quantos anos você pretende pagar a casa: '))
prestacao = valorCasa/(anos*12)

if prestacao > salario*0.30:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valorCasa,anos,prestacao))
    print('O emprestimo foi negado!')
else:
    print('O emprestimo foi aprovado e o valor das parcelas seram de R${:.2f}'.format(prestacao))