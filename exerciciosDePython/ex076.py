'''Crie um programa que leia uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listragem de preços organizado os dados de maneira tabular'''

produto = ('leite',3.50,'achocolatado',4.75,'Pão',1,'manteiga',4,'bolacha',2.75)

print('-'*40)
print('LISTA DE PREÇOS')
print('-'*40)
print(f'{produto[0]}...................R$   {produto[1]:.2f}')
print(f'{produto[2]}............R$   {produto[3]:.2f}')
print(f'{produto[4]}.....................R$   {produto[5]:.2f}')
print(f'{produto[6]}................R$   {produto[7]:.2f}')
print(f'{produto[8]}.................R$   {produto[9]:.2f}')
print('-'*40)

'''Este método usado não é indicado, deveria ter usado for para melhorar o código
correção:
print('-'*40)
print(f'{"Listagem de preços"}':^40)
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)'''