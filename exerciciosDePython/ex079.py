'''Crie um programa onde o usuário possa digitar vários valores numéricos e caadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.'''

lista = []
while True:
    num = int(input('Digite um valor para a lista: '))
    if num in lista:
        print('Este número já existe na lista!')
    else:
        print('O número foi adicionado com sucesso!')
        lista.append(num)
    cont = str(input('Deseja continuar[S/N]: '))[0].strip().upper()
    if cont in 'Nn':
        break

lista.sort()
print(f'A sua lista é:{lista}')