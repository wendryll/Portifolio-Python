from tkinter import *  #importando o tkinter
import mysql.connector #importando o conector com o banco de dados SQL

#conexão com banco de dados
db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="teste") #conecta com a base de dados
cursor = db_connection.cursor() #vai executar os comandos SQL

#função
def enviar():
    try:
        sql = "INSERT INTO usuarios (usuario,senha) VALUES (%s,%s)" #comando SQL
        usuario = usuario_text.get() #obtendo o valor do Entry
        senha = senha_text.get()     #obtendo o valor do Entry
        values = (usuario,senha)     #passando os valores do Entry para uma tupla
        cursor.execute(sql,values)   #passando a tupla para executar no seu banco de dados 
        usuario_text.delete(first=0,last=END)
        senha_text.delete(first=0,last=END)
    except:
        label_except = Label(janela,text="Ocorreu um erro! Tente novamente.").grid(row=3,column=1)
    else:
        label_else = Label(janela,text="Cadastrado com sucesso!").grid(row=3,column=1)


#janela
janela = Tk()
janela.title("cadastrar")
janela.geometry('200x100+250+250')
usuario_label = Label(janela,text='Usuario:').grid(row=0,column=0)
senha_label = Label(janela,text='Senha:').grid(row=1,column=0)
usuario_text = Entry(janela)
usuario_text.focus()
senha_text = Entry(janela)
bnt = Button(janela,text='confirm',command=enviar).grid(row=2,column=1)
#layout
#sempre crie e depois posicione as Entrys da sua página caso contrario ocorrerá um erro!
usuario_text.grid(row=0,column=1)
senha_text.grid(row=1,column=1)
janela.mainloop()