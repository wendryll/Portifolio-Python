#escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milímetros 
valor = float(input('Digite um valor em metros: '))
print('O valor {} em milimetros é {}'.format(valor,valor*1000))
print('O valor {} em centimetros é {}'.format(valor,valor*100))
print('O valor {} em decimetro é {}'.format(valor,valor*10))
print('O valor {} em decâmetros é {}'.format(valor,valor/10))
print('O valor {} em hectômetro é {}'.format(valor,valor/100))
print('O valor {} em quilômetro é {}'.format(valor,valor/1000))