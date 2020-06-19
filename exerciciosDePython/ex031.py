#Desenvolva um programa que pergunte a distância de uma viagem em Km.Calcule  preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = int(input('Digite a distancia da sua viajem em KM: '))
if distancia <= 200:
    print('O valor da passagem será de R${:.2f} para a distandia de {}Km'.format((distancia*0.50),distancia))
else:
    print('O valor da passagem será de R${:.2f} para a distancia de {}Km'.format((distancia*0.45),distancia))