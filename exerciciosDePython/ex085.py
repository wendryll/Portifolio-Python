'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares.No final mostre os valores pares e impares em ordem crescente.'''

imp = list()
par = list()
num = list()

for i in range(0,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        imp.append(numero)
num.append(par[:])
num.append(imp[:])
print(f'os números pares são {num[0]} e os ímpares {num[1]}')