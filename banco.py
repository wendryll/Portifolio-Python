"""Programa que manipula um banco de dados MySQL"""

import mysql.connector
def mensagem(msg):
    print('='*50)
    print(msg)
    print('='*50)
def menu():
    print("="*50)
    print("MENU".center(50))
    print("="*50)
    print('1 - Banco de dados')
    print('2 - Tabelas')
    print('3 - exibir dados da tabela')
    print('4 - Inserindo dados na tabela')
    print('5 - Sair')

def entrada(msg):
    global op
    try:
        op = int(input(msg))
    except:
        print("ERRO! Entre com um valor inteiro valido :(")
    else:
        return op

#variaveis 
op = ''

#conectando com o banco de dados 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="cadastro"
)
mycursor = mydb.cursor()

while True:
    menu()
    entrada("Digite a sua opção: ")
    if op == 1:
        mycursor.execute("show databases")
        #exibindo cada banco de dados do MySQL
        mensagem('Bancos de dados disponiveis')
        for i in mycursor:
            print(i)
    elif op == 2:
        mycursor.execute("show tables")
        #exibindo cada tabela do banco de dados
        mensagem('Tabelas disponiveis')
        for i in mycursor:
            print(i)
    elif op == 3:
        mensagem('Dados da tabela')
        tabela = str(input('Digite o nome da tabela: '))
        #exibindo dados da tabela 
        mycursor.execute(f"SELECT * FROM {tabela}")
        myresult = mycursor.fetchone()
        print('='*50)
        print(myresult)
    elif op == 4:
        mensagem("Inserindo dados na tabela Carros")
        sql = "INSERT INTO carros (modelo, ano) VALUES (%s, %s)"

        modelo = input("Qual o modelo do carro: ")
        ano = int(input("Qual o ano do carro: "))
        val = [(modelo, ano)]
        mycursor.executemany(sql,val)
        mydb.commit()
    elif op == 5:
        mensagem('programa encerrado...')
        break
    else:
        mensagem('ERRO! Digite uma opção válida')