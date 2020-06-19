'''Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. No final do programa, mostre:
-> A média de idade do grupo.       ->Quantas mulheres têm menos de 20 anos
-> Qual é o nome do homem mais velho'''

nome = []           #lista que armazena nomes
idade = []          #lista que armazena idades
sexo = []           #lista que armazena sexos
qtMulher = 0        #quantidade de mulheres
homemVelho = 0      #variavel para alocar o nome do homem mais velho
idadeVelho = 0      #variavel para alocar a idade do homem mais velho 
media = 0           #variavel para a média das idades
for i in range(0,4):      
    nome.append(str(input('Digite o nome da pessoa: ')))
    idade.append(int(input('Digite a idade da pessoa: ')))
    sexo.append(str(input('Digite o seu sexo, Masculino(m) ou Femenino(f): ')))
for i in range(0,4):
    if idade[i] < 20 and sexo[i] == 'f' or idade[i] < 20 and sexo == 'feminino':        #verificando quantidade de mulheres
        qtMulher += 1                                                                   #menores que 20 anos        
for i in range(0,4):
     media += idade[i]          #média
for i in range(0,4):
    if idade[i] > idade[i - 1]:        #nome e idade do homem mais velho
        homemVelho = nome[i]
        velhoIdade = idade[i]

print('A média de idades do grupo é de {}.'.format(media/4))
print('O nome do homem mais velho é {} e possuí {} anos.'.format(homemVelho,velhoIdade))
print('Há {} mulheres com menos de 20 anos.'.format(qtMulher))