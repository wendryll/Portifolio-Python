'''faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,com uma pausa de 1 segundo entre eles'''

import time

print('=-'*10,'Contagem regressiva até os fogos','-='*10)
for i in range(10,-1,-1):
    print(i)
    time.sleep(1)
print('*'*47)
print('=-'*10,'FOGOS','-='*10)
print('*'*47)