#-*-coding:utf-8-*-
#variaveis usadas no código
altura = 0
peso = 0
imc = 0


#funções
def calculo(altura,peso):                               #função para calcular o IMC de uma pessoa que recebe a altura e o peso
    altura = altura ** 2
    imc = peso / altura

def tabelaPesos(imc):                                   #função que verifica em qual categoria a sua faixa de peso está baseado no imc
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc <= 24.9:
        print('Peso normal')
    elif imc <= 29.9:
        print('Sobre peso')
    elif imc <= 34.9:
        print('Obesidade grau 1')
    elif imc <=  39.9:
        print('Obesidade grau 2')
    else:
        print('Obesidade grau 3')

def entradaDeDados():
    print('Vamos calcular o Imc')
    print('--------------------')
    nome = input('Digite o seu nome: ')                 #recolhendo o nome da pessoa por meio do input
    altura = float(input('Digite a sua altura: '))      #recolhendo a altura da pessoa por meio do input
    peso = float(input('Digite o seu peso: '))          #recolhendo o peso da pessoa por meio do input
    calculo(altura,peso)                                #chamando a função que calcula o imc
    print('o IMC de ' , nome)                           #exibindo IMC e o nome da pessoa
    tabelaPesos(imc)                                    #chamando a função de tabelas de pesos
    print('-------------------')

#chamadas de funções
entradaDeDados()