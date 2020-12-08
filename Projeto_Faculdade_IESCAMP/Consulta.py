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

def consultar():
    janela_consulta = Toplevel()
    #definindo geometria da janela info_window
    largura = 1300 #definindo a largura do formulario
    altura = 500  #definido a altura do formulario
    #resolução do nosso sistema
    largura_screen = janela_consulta.winfo_screenwidth() #retorna o tamanho real da largura do monitor
    altura_screen = janela_consulta.winfo_screenheight() #retorna o tamanho real da altura do monitor
    #Posição da janela
    posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
    posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio
    #definir a geometry
    janela_consulta.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
    janela_consulta.resizable(False,False) #definindo que a janela não é redimencionavel
    
    #criando objeto notebook para a criação de janelas
    guia = ttk.Notebook(janela_consulta,width=1300,height=800)
    #Criando frames das guias
    guia_cnpj = Frame(guia)
    guia_razao_social = Frame(guia)
    #Adicionando guias a janela
    guia.add(guia_cnpj,text='Consulta por CNPJ')
    guia.add(guia_razao_social,text='Consulta por Razão Social')
    guia.pack(expand=1,fill='both')

    """
    -> Conteudo GUIA: CNPJ
    """
    labelframe_cnpj = LabelFrame(guia_cnpj,text='CNPJ')
    labelframe_cnpj.pack(fill="both",expand="yes",padx=20,pady=20)
    #tela de exibição de conteudo
    tv_cnpj = ttk.Treeview(labelframe_cnpj,columns=('Id',
                                            'Razão social',
                                            'Nome fantasia',
                                            'Cnpj',
                                            'Inscrição Estadual',
                                            'Inscrição Municipal',
                                            'Municipio',
                                            'Uf',
                                            'Telefone',
                                            'Email')
                                            ,show='headings')
    tv_cnpj.column('Id',minwidth=0,width=50)
    tv_cnpj.column('Razão social',minwidth=0,width=150)
    tv_cnpj.column('Nome fantasia',minwidth=0,width=150)
    tv_cnpj.column('Cnpj',minwidth=0,width=80)
    tv_cnpj.column("Inscrição Estadual",minwidth=0,width=150)
    tv_cnpj.column("Inscrição Municipal",minwidth=0,width=150)
    tv_cnpj.column("Municipio",minwidth=0,width=80)
    tv_cnpj.column("Uf",minwidth=0,width=50)
    tv_cnpj.column("Telefone",minwidth=0,width=80)
    tv_cnpj.column("Email",minwidth=0,width=150)

    tv_cnpj.heading('Id',text='ID')
    tv_cnpj.heading('Razão social',text='RAZÃO SOCIAL')
    tv_cnpj.heading('Nome fantasia',text='NOME FANTASIA')
    tv_cnpj.heading('Cnpj',text='CNPJ')
    tv_cnpj.heading("Inscrição Estadual",text='INSCRIÇÃO ESTADUAL')
    tv_cnpj.heading("Inscrição Municipal",text='INSCRIÇÃO MUNICIPAL')
    tv_cnpj.heading("Municipio",text='MUNICIPIO')
    tv_cnpj.heading('Uf',text='UF')
    tv_cnpj.heading("Telefone",text='TELEFONE')
    tv_cnpj.heading('Email',text='EMAIL')
    tv_cnpj.pack()

    """
        Campo reservado para def
    """

    def consultar_cnpj():
        tv_cnpj.delete(*tv_cnpj.get_children())
        sql = f"select cliente.id_cliente,cliente.razao_social,cliente.nome_fantasia,cliente.cnpj,inscricao_estadual,cliente.inscricao_municipal,municipio.nome_municipio,municipio.uf, contato.telefone, contato.email from cliente inner join municipio on municipio.id_municipio = cliente.municipio inner join contato on  contato.id_contato = cliente.contato where cnpj = {entry_cnpj.get().upper()}"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        linhas = resultado
        for i in linhas:
            tv_cnpj.insert("","end",values=i)

        db_connection.commit()
    def consultar_razao_social():
        tv_razao_social.delete(*tv_razao_social.get_children())
        sql = f"select cliente.id_cliente,cliente.razao_social,cliente.nome_fantasia,cliente.cnpj,inscricao_estadual,cliente.inscricao_municipal,municipio.nome_municipio,municipio.uf, contato.telefone, contato.email from cliente inner join municipio on municipio.id_municipio = cliente.municipio inner join contato on  contato.id_contato = cliente.contato where razao_social = '{entry_razao_social.get().upper()}'"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        linhas = resultado
        for i in linhas:
            tv_razao_social.insert("","end",values=i)

        db_connection.commit()   
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
    validando_numero = janela_consulta.register(validar_numero)

    #widgets
    labelframe_dados = LabelFrame(labelframe_cnpj,text='Digite os dados do cliente')
    label_cnpj = Label(labelframe_dados,text='CNPJ',font='arial 10')
    entry_cnpj = Entry(labelframe_dados,validate='key',validatecommand=(validando_numero,"%S"))
    bnt_consulta = Button(labelframe_dados,text='consultar',command=consultar_cnpj)

    #Posicionamento
    labelframe_dados.pack(fill="both",expand="yes",padx=20,pady=20)
    label_cnpj.grid(row=1,column=0,padx=5,pady=5)
    entry_cnpj.grid(row=1,column=1,padx=5,pady=5)
    bnt_consulta.grid(row=1,column=2,padx=5,pady=5)

    """
    ->Conteudo GUIA:Razão social
    """
    labelframe_razao_social = LabelFrame(guia_razao_social,text='Razão social')
    labelframe_razao_social.pack(fill="both",expand="yes",padx=20,pady=20)

    tv_razao_social = ttk.Treeview(labelframe_razao_social,columns=('Id',
                                                                    'Razão social',
                                                                    'Nome fantasia',
                                                                    'Cnpj',
                                                                    'Inscrição Estadual',
                                                                    'Inscrição Municipal',
                                                                    'Municipio',
                                                                    'Uf',
                                                                    'Telefone',
                                                                    'Email')
                                                                    ,show='headings')
    tv_razao_social.column('Id',minwidth=0,width=50)
    tv_razao_social.column('Razão social',minwidth=0,width=150)
    tv_razao_social.column('Nome fantasia',minwidth=0,width=150)
    tv_razao_social.column('Cnpj',minwidth=0,width=80)
    tv_razao_social.column("Inscrição Estadual",minwidth=0,width=150)
    tv_razao_social.column("Inscrição Municipal",minwidth=0,width=150)
    tv_razao_social.column("Municipio",minwidth=0,width=80)
    tv_razao_social.column("Uf",minwidth=0,width=50)
    tv_razao_social.column("Telefone",minwidth=0,width=80)
    tv_razao_social.column("Email",minwidth=0,width=150)

    tv_razao_social.heading('Id',text='ID')
    tv_razao_social.heading('Razão social',text='RAZÃO SOCIAL')
    tv_razao_social.heading('Nome fantasia',text='NOME FANTASIA')
    tv_razao_social.heading('Cnpj',text='CNPJ')
    tv_razao_social.heading("Inscrição Estadual",text='INSCRIÇÃO ESTADUAL')
    tv_razao_social.heading("Inscrição Municipal",text='INSCRIÇÃO MUNICIPAL')
    tv_razao_social.heading("Municipio",text='MUNICIPIO')
    tv_razao_social.heading('Uf',text='UF')
    tv_razao_social.heading("Telefone",text='TELEFONE')
    tv_razao_social.heading('Email',text='EMAIL')
    tv_razao_social.pack()
    #widgets
    labelframe_dados = LabelFrame(labelframe_razao_social,text='Digite os dados do cliente')
    label_razao_social = Label(labelframe_dados,text='Razão Social:',font='arial 10')
    entry_razao_social = Entry(labelframe_dados,width=80)
    bnt_consulta = Button(labelframe_dados,text='consultar',command=consultar_razao_social)

    #Posicionamento
    labelframe_dados.pack(fill="both",expand="yes",padx=20,pady=20)
    label_razao_social.grid(row=1,column=0,padx=5,pady=5)
    entry_razao_social.grid(row=1,column=1,padx=5,pady=5)
    bnt_consulta.grid(row=1,column=2,padx=5,pady=5)

    janela_consulta.mainloop()