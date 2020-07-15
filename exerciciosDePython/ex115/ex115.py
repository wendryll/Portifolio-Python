"""Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

def menu():
    print('-'*50)
    print('MENU PRINCIPAL'.center(50))
    print('-'*50)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do sistema')
    print('-'*50)

def final():
    print('-'*50)
    print('Encerrando o programa'.center(50))
    print('-'*50)

def leitura(arquivo, metodo):
    print('-'*50)
    ler = open(arquivo,metodo)
    print('Pessoas cadastradas'.center(50))
    print('-'*50)
    ler = ler.read()

sair = False
while not sair:
    menu()
    try:
        opcao = int(input('Digite o valor da sua opção: '))
    except:
        print('ERRO: Digite um valor inteiro válido! :(')
    
    if opcao == 1:
        leitura= open("cadastro.txt","r")
        print(leitura.readlines())

    elif opcao == 2:
        arquivo = open("cadastro.txt","a")
        nome = str(input('Nome completo: '))
        idade = str(input('Idade: '))
        arquivo.write(nome)
        arquivo.write(idade)
    elif opcao == 3:
        final()
        sair = True
