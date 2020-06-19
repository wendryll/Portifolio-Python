'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
-à vista dinheiro/cheque 10% de desconto.        -em até 2x no cartão preço normal
-à vista no cartão 5% de desconto                -3x ou mais no cartão 20% de juros'''

print('='*30,'LOJAS GUANABARA','='*30 )
print('\n')
valor = float(input('Digite o valor a ser pago: R$'))
print('\n')
print('FORMAS DE PAGAMENTOS')
print('[1] Pagamento à vista dinheiro/cheque')
print('[2] Pagamento à vista cartão')
print('[3] Pagamento em 2x no cartão')
print('[4] Pagamento 3x ou mais vezes no cartão')
print('\n')
op = int(input('Qual a sua opção: '))
if op == 1:
    desconto = (valor - (valor*0.10))
    print('Sua compra será à vista e receberá dez porcento de desconto')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,desconto))
elif op == 2:
    desconto = (valor - (valor*0.05))
    print('Sua compra será à vista e receberá cinco porcento de desconto')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,desconto))
elif op == 3:
    parcela = (valor/2)
    print('Sua compra será parcelada em 2x no cartão.')
    print('Sua compra de R${:.2f} vai custar duas parcelas de R${:.2f}.'.format(valor,parcela))
elif op == 4:
    qtParcela = int(input('Quantidade de parcelas: '))
    juros = (valor + (valor*0.20))
    parcela = juros/qtParcela
    print('Sua compra será em {:.2f}x de R${:.2f} COM JUROS'.format(qtParcela,parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} COM JUROS'.format(valor,juros))
else:
    print('Opção invalida!')

