#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de quilometros rodados: '))
dia = int(input('Digite a quantidade de dias que o carro ficou alugado: '))
pagamento = (60*dia)+(km*0.15)
print('O carro que ficou alugado {} dias e percorreu {}Km terá um preço a ser pago de R${}'.format(dia,km,pagamento))