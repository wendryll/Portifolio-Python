'''Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o contúdo das três listas geradas.'''

lista = []
imp = []
par = []

while True:
    lista.append(int(input('Digite um valor para a lista: ')))
    cont = str(input('Deseja continuar[S/N]: '))[0].strip().upper()
    if cont in 'N':
        break

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        imp.append(lista[i])

print(f'A sua lista é {lista}')
print(f'Os números ímpares da lista são: {imp}')
print(f'Os números pares da lista são: {par}')