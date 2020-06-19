'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5:Abaixo de peso  -25 até 30:Sobrepeso   -Acima de 40:Obesidade mórbida
-Entre 18.5 a 25:Peso ideal     -30 até 40:Obesidade'''

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso/(altura**2)

print('O seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')