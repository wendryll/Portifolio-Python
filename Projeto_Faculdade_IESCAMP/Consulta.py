from tkinter import *
from tkinter import ttk
import DadosValidacao
import mysql.connector #importando o conector com o banco de dados SQL
from mysql.connector.constants import ClientFlag
#banco de dados
db_connection = mysql.connector.connect(host=DadosValidacao.host,
                                        user=DadosValidacao.user,
                                        passwd=DadosValidacao.passwd,
                                        database=DadosValidacao.database) #conecta com a base de dados
cursor = db_connection.cursor() #vai executar os comandos SQL

def validar_numero(i):
    valido = i in DadosValidacao.numeros
    return valido

def consultar_cnpj():
    janela_consulta_cnpj = Toplevel()

    #definindo geometria da janela info_window
    largura = 500 #definindo a largura do formulario
    altura = 500  #definido a altura do formulario
    #resolução do nosso sistema
    largura_screen = janela_consulta_cnpj.winfo_screenwidth() #retorna o tamanho real da largura do monitor
    altura_screen = janela_consulta_cnpj.winfo_screenheight() #retorna o tamanho real da altura do monitor
    #Posição da janela
    posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
    posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio
    #definir a geometry
    janela_consulta_cnpj.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
    janela_consulta_cnpj.resizable(False,False) #definindo que a janela não é redimencionavel
    
    listbox = Listbox(janela_consulta_cnpj,width=85,height=90)
    listbox.pack()
    
    janela_consulta_cnpj.mainloop()


def consultar_razao_social():
    pass

def consultar():
    janela_consultar = Toplevel()
    #definindo geometria da janela info_window
    largura = 300 #definindo a largura do formulario
    altura = 100  #definido a altura do formulario
    #resolução do nosso sistema
    largura_screen = janela_consultar.winfo_screenwidth() #retorna o tamanho real da largura do monitor
    altura_screen = janela_consultar.winfo_screenheight() #retorna o tamanho real da altura do monitor

    #Posição da janela
    posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
    posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

    #definir a geometry
    janela_consultar.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
    janela_consultar.resizable(False,False) #definindo que a janela não é redimencionavel  
    
    #variaveis 
    validando_numero = janela_consultar.register(validar_numero)

    notebook = ttk.Notebook(janela_consultar)
    
    tab_cnpj = ttk.Frame(notebook)
    notebook.add(tab_cnpj,text='consulta cnpj')
    notebook.pack(expand=1,fill='both')

    tab_razao_social = ttk.Frame(notebook)
    notebook.add(tab_razao_social,text='consulta razão social')
    notebook.pack(expand=1,fill='both')

    label_cnpj = Label(tab_cnpj,text='consultar por CNPJ:')
    entry_cnpj = Entry(tab_cnpj,validate='key',validatecommand=(validando_numero,"%S"),width=15)
    bnt_cnpj = Button(tab_cnpj,text='consultar',command=consultar_cnpj)
    label_cnpj.grid(row=0,column=0,sticky=W)
    entry_cnpj.grid(row=0,column=1,sticky=W)
    bnt_cnpj.grid(row=1,column=1)

    label_razao_social = Label(tab_razao_social,text='consultar por Razão Social:')
    entry_razao_social = Entry(tab_razao_social,width=30)
    bnt_razao_social = Button(tab_razao_social,text='consultar',command=consultar_razao_social)
    label_razao_social.grid(row=0,column=0,sticky=W)
    entry_razao_social.grid(row=0,column=1,sticky=W)
    bnt_razao_social.grid(row=2,column=1)

    janela_consultar.mainloop()