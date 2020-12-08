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

def ListarCliente():
    janela_listarCliente = Toplevel()
    #definindo geometria da janela info_window
    largura = 800 #definindo a largura do formulario
    altura = 500  #definido a altura do formulario
    #resolução do nosso sistema
    largura_screen = janela_listarCliente.winfo_screenwidth() #retorna o tamanho real da largura do monitor
    altura_screen = janela_listarCliente.winfo_screenheight() #retorna o tamanho real da altura do monitor
    #Posição da janela
    posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
    posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio
    #definir a geometry
    janela_listarCliente.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
    janela_listarCliente.resizable(False,False) #definindo que a janela não é redimencionavel

    frame_listar = LabelFrame(janela_listarCliente,text='Clientes')
    frame_listar.pack(fill="both",expand="yes",padx=10,pady=10)

    tv = ttk.Treeview(frame_listar,columns=('Id',
                                            'Razão social',
                                            'Nome fantasia',
                                            'Cnpj'),
                                            show='headings')
    
    #exibindo os dados dentro do treeview

    """
        Area reservada para def
    """

    def exibir_cliente():
        tv.delete(*tv.get_children())
        sql = "SELECT id_cliente,razao_social,nome_fantasia,cnpj from cliente ORDER BY id_cliente"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        linhas = resultado
        for i in linhas:
            tv.insert("","end",values=i)
    
    def filtrar_cliente():
        tv.delete(*tv.get_children())
        sql = f"SELECT  id_cliente,razao_social,nome_fantasia,cnpj from cliente WHERE razao_social LIKE '%" + entry_filtro.get().upper() + "%'"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        linhas = resultado
        for i in linhas:
            tv.insert("","end",values=i)
    def exclui():
        sql = f"DELETE FROM cliente WHERE id_cliente = '{entry_excluir.get().upper()}'"
        cursor.execute(sql)
        entry_excluir.delete(0,END)
        exibir_cliente()

    def validar_numero(i):
        """
        ->Validar_numero:
            -parametro i corresponde a qualquer coisa digitada pelo usuario
            -funcao que verifica se o que foi digitado pelo usuario esta contido dentro da variavel numeros
            em caso afirmativo o valor é devolvido, caso contrario o valor nao é devolvido
        """
        valido = i in DadosValidacao.numeros
        return valido

    #variaveis
    validando_numero = janela_listarCliente.register(validar_numero)

    """
        Tela de exibição dos dados do cliente
    """
    #adicionando Colunas
    tv.column('Id',minwidth=0,width=50)
    tv.column('Razão social',minwidth=0,width=250)
    tv.column('Nome fantasia',minwidth=0,width=250)
    tv.column('Cnpj',minwidth=0,width=50)
    #adicionando cabeçalho das colunas
    tv.heading( 'Id',text='ID')
    tv.heading( 'Razão social',text='RAZÃO SOCIAL')
    tv.heading( 'Nome fantasia',text='NOME FANTASIA')
    tv.heading( 'Cnpj',text='CNPJ')
    tv.pack()
    exibir_cliente()

    #frame filtro
    frame_filtro = LabelFrame(frame_listar,text='Pesquisar Clientes',height=30)
    frame_filtro.pack(fill="both",expand="yes",padx=10,pady=10)
    #widgets
    label_filtro = Label(frame_filtro,text='razão social',font='arial 10')
    entry_filtro = Entry(frame_filtro,width=30)
    bnt_pesquisar = Button(frame_filtro,text='Filtrar',command=filtrar_cliente)
    bnt_mostrar = Button(frame_filtro,text='Exibir Todos',command=exibir_cliente)

    label_excluir = Label(frame_filtro,text='Excluir por ID do cliente',font='arial 10')
    entry_excluir = Entry(frame_filtro,validate='key',validatecommand=(validando_numero,"%S"),width=30)
    bnt_exclui = Button(frame_filtro,text='excluir',command=exclui)    
    #posicionamento
    label_filtro.grid(row=0,column=0,padx=5,pady=5,sticky=W)
    entry_filtro.grid(row=0,column=1,padx=5,pady=5,sticky=W)
    bnt_pesquisar.grid(row=0,column=2,padx=5,pady=5,sticky=W)
    bnt_mostrar.grid(row=0,column=3,padx=5,pady=5,sticky=W)
    label_excluir.grid(row=1,column=0,padx=5,pady=5,sticky=W)
    entry_excluir.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    bnt_exclui.grid(row=1,column=2,padx=5,pady=5,sticky=W)
    janela_listarCliente.mainloop()