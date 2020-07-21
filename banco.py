"""Verifcando banco de dados com python """

import mysql.connector

def tabelas():
    mycrusor.execute('show tables')
    print("="*50)
    print('TABELAS'.center(50))
    print('='*50)
    for i in mycrusor:
        print(i)
    
def menu():
    print("="*50)
    print("2 - Exibir tabelas")
    print("="*50)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database='cadastro'
    )
mycrusor = mydb.cursor()
