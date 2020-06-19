#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$3,27

valor = float(input('Digite a quantidade de dinheiro que você possui: R$'))
print('Você possui R${:.2f} e com este valor você pode comprar US${:.2f} Dólares'.format(valor,(valor/3.27)))