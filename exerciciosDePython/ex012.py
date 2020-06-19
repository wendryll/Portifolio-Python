#Faça um algoritmmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
desconto = preco*(5/100)
print('O produto que custa {:.2f} com desconto de cinco porcento custa: R${:.2f}'.format(preco,preco-desconto))