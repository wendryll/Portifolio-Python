from tkinter import *
import DadosValidacao
import mysql.connector #importando o conector com o banco de dados SQL
#banco de dados
db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="vendas") #conecta com a base de dados
cursor = db_connection.cursor() #vai executar os comandos SQL

#função
def validar_numero(i):
    valido = i in DadosValidacao.numeros
    return valido

def consulta():
    """
    ->Validar_numero:
        -parametro i corresponde a qualquer coisa digitada pelo usuario
        -funcao que verifica se o que foi digitado pelo usuario esta contido dentro da variavel numeros
        em caso afirmativo o valor é devolvido, caso contrario o valor nao é devolvido
    """
    janela_cliente = Toplevel()
    janela_cliente.title('Cliente')
    dados_cliente = Listbox(janela_cliente)

    #variaveis globais
""" Alterar Apenas testes
    cursor.execute('SELECT uf FROM uf') #comando select do MySQL
    myresult = cursor.fetchall()
    conteudo = [] #lista com uf de uma tabela do banco de dados
    for i in myresult:      #for que percorre o conteudo da tabela uf do banco de dados
        conteudo.append(i)
    for cont in conteudo:
        dados_cliente.insert(END,cont)
        dados_cliente.pack()
    janela_cliente.mainloop()"""
    

def Consultar():
    janela_consulta = Toplevel()
    janela_consulta.title('Consultar')
    largura = 250 #definindo a largura do formulario
    altura = 100  #definido a altura do formulario
        
    #resolução do nosso sistema
    largura_screen = janela_consulta.winfo_screenwidth() #retorna o tamanho real da largura do monitor
    altura_screen = janela_consulta.winfo_screenheight() #retorna o tamanho real da altura do monitor

    #Posição da janela
    posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
    posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

    #definir a geometry
    janela_consulta.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
    janela_consulta.resizable(False,False) #definindo que a janela não é redimencionavel

    #variaveis globais
    validando_numero = janela_consulta.register(validar_numero)

    label_cnpj = Label(janela_consulta,text='Consultar cliente por CNPJ:')

    entry_cnpj = Entry(janela_consulta,validate='key',validatecommand=(validando_numero,"%S"),width=15)

    bnt_consultar = Button(janela_consulta,text='consultar',command=consulta)

    label_cnpj.grid(row=0,column=0,sticky=W)
    entry_cnpj.grid(row=0,column=1,sticky=W)
    bnt_consultar.grid(row=1,column=1,sticky=W)
    janela_consulta.mainloop()