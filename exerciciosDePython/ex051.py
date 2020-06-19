'''Desenvolva um programa que leia o primeiro termo e a razãode uma PA.No final, mostre os 10 primeiros termos dessa progrssão'''
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = p +(10-1)*r
for i in range(p,decimo + r,r):
    print(i)
print('Fim')