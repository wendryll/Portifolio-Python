#Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
velocidade = int(input('Digite a velocidade a sua velocidade atual:  '))

if velocidade > 80:
    print('Você ultrapassou o limite de velocidade, receberá uma multa de R${}.'.format((velocidade-80)*7.00))
else:
    print('Você está no limite permitido, tenha um bom dia e dirija com segurança.')