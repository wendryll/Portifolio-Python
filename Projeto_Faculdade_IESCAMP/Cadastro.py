from tkinter import * #importando a biblioteca tkinter
from tkinter import ttk #importando ttk para criação do combobox
from tkinter import messagebox
import DadosValidacao #importando arquivo com as variaveis de validação
import mysql.connector #importando o conector com o banco de dados SQL

#banco de dados
db_connection = mysql.connector.connect(host=DadosValidacao.host,
                                        user=DadosValidacao.user,
                                        passwd=DadosValidacao.passwd,
                                        database=DadosValidacao.database) #conecta com a base de dados
cursor = db_connection.cursor() #vai executar os comandos SQL

#funções

def validar_numero(i):
    """
    ->Validar_numero:
        -parametro i corresponde a qualquer coisa digitada pelo usuario
        -funcao que verifica se o que foi digitado pelo usuario esta contido dentro da variavel numeros
        em caso afirmativo o valor é devolvido, caso contrario o valor nao é devolvido
    """
    valido = i in DadosValidacao.numeros
    return valido

def validar_email(i):
    """
    ->validar_email:
        -parametro i corresponde a qualquer coisa digitada pelo usuario
        -funcao que verifica se o que foi digitado pelo usuario esta contido dentro das variaveis, numeros, letras, simbolo_email,
        em caso afirmativo o valor é devolvido, caso contrario o valor nao é devolvido
    """
    valido = i in DadosValidacao.letras + DadosValidacao.letras.upper() + DadosValidacao.numeros + DadosValidacao.simbolo_email
    return valido

def validar_url(i):
    """
    ->validar_url:
        -parametro i corresponde a qualquer coisa digitada pelo usuario
        -funcao que verifica se o que foi digitado pelo usuario esta contido dentro das variaveis, numeros, letras, simbolo_url,
        em caso afirmativo o valor é devolvido, caso contrario o valor nao é devolvido
    """
    valido = i in DadosValidacao.letras+ DadosValidacao.letras.upper() + DadosValidacao.numeros + DadosValidacao.simbolo_url
    return valido

def validar_letra_numero(i):
    """
    -parametro i corresponde a qualquer coisa digitada pelo usuario
        -funcao que verifica se o que foi digitado pelo usuario esta contido dentro da variaveis, numeros, letras,
        em caso afirmativo o valor é devolvido, caso contrario o valor nao é devolvido
    """
    valido = i in DadosValidacao.letras + DadosValidacao.numeros
    return valido

def janela_confirma():
    """
    ->Exibe uma caixa de span na tela confirmando o cadastro do cliente, com um botão para click que fecha a janela
    """
    messagebox.showinfo("Confirmação de cadastro", "O cadastro do cliente, foi realizado com sucesso!")

def Cadastra_cliente():
    """
    -> Cadastrar_cliente:
        - funcao que executa uma janela tkinter de cadastramento de clientes
    """

    #janela
    janela_cadastro = Toplevel()
    janela_cadastro.title =("Cadastro de Clientes")
    #definindo geometria da janela
    largura = 1300 #definindo a largura do formulario
    altura = 350  #definido a altura do formulario
    

    #resolução do nosso sistema
    largura_screen = janela_cadastro.winfo_screenwidth() #retorna o tamanho real da largura do monitor
    altura_screen = janela_cadastro.winfo_screenheight() #retorna o tamanho real da altura do monitor

    #Posição da janela
    posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
    posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

    #definir a geometry
    janela_cadastro.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
    janela_cadastro.resizable(False,False) #definindo que a janela não é redimencionavel
    
    #label Frame
    label_frame = LabelFrame(janela_cadastro,text='Dados do Cliente')
    label_frame.pack(fill="both",expand="yes",padx=10,pady=10)
    
    #variaveis
    """
        Espaço reservado para a criação de variaveis de uso global no código
    """
    valor_whatsapp = IntVar()
    validando_numero = janela_cadastro.register(validar_numero)
    validando_email = janela_cadastro.register(validar_email)
    validando_url = janela_cadastro.register(validar_url)
    validando_letra_numero = janela_cadastro.register(validar_letra_numero)

    #widgets
    """
        Espaço reservado para a criação de labels(tkinters)
    """
    label_razao_social = Label(label_frame, text="Razão Social",font='arial 10')
    label_nome_fantasia = Label(label_frame, text="Nome Fantasia:",font='arial 10')
    label_cnpj = Label(label_frame, text="CNPJ:",font='arial 10')
    label_inscricao_estadual = Label(label_frame, text="Inscrição Estadual:",font='arial 10')
    label_inscricao_municipal = Label(label_frame, text="Inscrição Municipal:",font='arial 10')
    label_rua = Label(label_frame, text="Rua:",font='arial 10')
    label_numero = Label(label_frame, text="Número:",font='arial 10')
    label_complemento = Label(label_frame, text="Complemento:",font='arial 10')
    label_bairro = Label(label_frame, text="Bairro:",font='arial 10')
    label_municipio = Label(label_frame, text="Municipio:",font='arial 10')
    label_uf = Label(label_frame, text="UF:",font='arial 10')
    label_cep = Label(label_frame, text="CEP:",font='arial 10')
    label_telefone = Label(label_frame, text="Telefone:",font='arial 10')
    label_celular = Label(label_frame,text="Celular:",font='arial 10')
    label_url = Label(label_frame, text="URL:",font='arial 10')
    label_email = Label(label_frame, text="E-mail:",font='arial 10')
    """
        Espaço reservado para a criação de entrys(tkinters)
    """
    entry_razao_social = Entry(label_frame,width=80)
    entry_nome_fantasia = Entry(label_frame,width=80)
    entry_cnpj = Entry(label_frame,validate='key',validatecommand=(validando_numero,"%S"),width=15)
    entry_inscricao_estadual = Entry(label_frame,validate='key',validatecommand=(validando_numero,"%S"),width=40)
    entry_inscricao_municipal = Entry(label_frame,validate='key',validatecommand=(validando_numero,"%S"),width=40)
    entry_rua = Entry(label_frame,width=40,validate="key",validatecommand=(validar_letra_numero,"%S"))
    entry_numero = Entry(label_frame,validate='key',validatecommand=(validando_numero,"%S"),width=10)
    entry_complemento = Entry(label_frame,width=20,validate="key",validatecommand=(validar_letra_numero,"%S"))
    entry_bairro = Entry(label_frame,width=20,validate="key",validatecommand=(validar_letra_numero,"%S"))
    entry_municipio = Entry(label_frame,width=40,validate="key",validatecommand=(validar_letra_numero,"%S"))
    entry_cep = Entry(label_frame,validate='key',validatecommand=(validando_numero,"%S"),width=13)
    entry_telefone = Entry(label_frame,validate='key',validatecommand=(validando_numero,"%S"),width=13)
    entry_celular = Entry(label_frame,validate='key',validatecommand=(validando_numero,"%S"),width=13)
    entry_url = Entry(label_frame,width=40,validate='key',validatecommand=(validando_url,"%S"))
    entry_email = Entry(label_frame,validate='key',validatecommand=(validando_email,"%S"),width=40)
    
    """
        Espaço reservado para a criação de checkbutton(tkinter)
    """
    bnt_whatsapp = Checkbutton(label_frame,text="Whatsapp:",variable=valor_whatsapp).grid(row=8,column=5)

    #combobox
    """
        Espaço reservado para a criação de um combobox que busca os dados dentro de uma tabela da base de dados para 
        a exibição ao usuario.
    """
    box_uf = ttk.Combobox(label_frame)#instanciando o objeto combobox
    box_uf['state'] = 'readonly' #deixando o compo sem digitação para o usuario
    cursor.execute('SELECT uf FROM uf') #comando select do MySQL
    myresult = cursor.fetchall()
    lista_uf = [] #lista com uf de uma tabela do banco de dados
    for i in myresult:      #for que percorre o conteudo da tabela uf do banco de dados
        lista_uf.append(i)  #adicionando o conteudo da tabela dentro de uma lista
    box_uf['values'] = lista_uf #atribuindo a lista ao combobox

    """
        Area reservada para a função salvar que salva os dados dentro de um banco de dados
    """
    
    def salvar():
        if entry_razao_social.get() == '' or entry_nome_fantasia.get() == '' or entry_cnpj.get() == None or entry_inscricao_estadual.get() == None or entry_inscricao_municipal.get() == None or entry_rua.get() == '' or entry_bairro.get() == '' or entry_municipio.get() == '' or entry_cep.get() == None or entry_telefone.get() == None or entry_email.get == '':
            entry_razao_social['bg'] = 'red'
            entry_nome_fantasia['bg'] = 'red'
            entry_cnpj['bg'] = 'red'
            entry_inscricao_estadual['bg'] = 'red'
            entry_inscricao_municipal['bg'] = 'red'
            entry_rua['bg'] = 'red'
            entry_bairro['bg'] = 'red'
            entry_municipio['bg'] = 'red'
            entry_cep['bg'] = 'red'
            entry_telefone['bg'] = 'red'
            entry_email['bg'] =      'red'
        else:
            """
                Espaço reservado para a gravação de dados no SGBD (MySQL)
            """
            #dados do contato
            if valor_whatsapp == 1:
                whatsapp = 'N'
            else:
                whatsapp = 'S'

            columns = "telefone, \
                        celular, \
                        email, \
                        url, \
                        whatsapp"

            values = f"'{entry_telefone.get().upper()}',\
                        '{entry_celular.get().upper()}', \
                        '{entry_email.get().upper()}', \
                        '{entry_url.get().upper()}', \
                        '{whatsapp.upper()}'"

            sql = f"INSERT INTO contato({columns}) VALUES({values})"
            cursor.execute(sql)
            #obtendo o ID que acabou de ser gerado no insert acima
            id_contato = cursor.lastrowid

            #dados do municipio
            columns = "nome_municipio, \
                        rua, \
                        numero, \
                        complemento, \
                        bairro, \
                        cep, \
                        uf"
            
            values = f"'{entry_municipio.get().upper()}', \
                        '{entry_rua.get().upper()}', \
                        '{entry_numero.get().upper()}', \
                        '{entry_complemento.get().upper()}', \
                        '{entry_bairro.get().upper()}', \
                        '{entry_cep.get().upper()}', \
                        '{box_uf.get().upper()}'"

            sql = f'INSERT INTO municipio({columns}) VALUES({values})'
            cursor.execute(sql)
            #obtendo o ID que acabou de ser gerado no insert acima
            id_municipio = cursor.lastrowid

            #Dados do cliente
            columns = "razao_social, \
                        nome_fantasia, \
                        cnpj, \
                        inscricao_estadual, \
                        inscricao_municipal, \
                        contato, \
                        municipio"
            
            values = f"'{entry_razao_social.get().upper()}',\
                        '{entry_nome_fantasia.get().upper()}', \
                        '{entry_cnpj.get().upper()}', \
                        '{entry_inscricao_estadual.get().upper()}', \
                        '{entry_inscricao_municipal.get().upper()}', \
                        '{id_contato}', \
                        '{id_municipio}'"
            
            sql = f"INSERT INTO cliente({columns}) VALUES({values})"
            cursor.execute(sql)

            db_connection.commit()
            db_connection.close()

            janela_cadastro.destroy()
            janela_confirma()

    """
        Espaço reservado para a criação de button(tkinter)
    """
    button_salvar = Button(label_frame, text="Salvar",command=salvar)

    #posicionamento de layout
    """
        Espaço reservado para o posicionamento de objetos dentro da janela
    """
    label_razao_social.grid(row=0,column=0,sticky=W)
    entry_razao_social.grid(row=0,column=1,sticky=W)
    label_nome_fantasia.grid(row=1,column=0,sticky=W)
    entry_nome_fantasia.grid(row=1,column=1,sticky=W)
    label_cnpj.grid(row=2,column=0,sticky=W)
    entry_cnpj.grid(row=2,column=1,sticky=W)
    label_inscricao_estadual.grid(row=3,column=0,sticky=W)
    entry_inscricao_estadual.grid(row=3,column=1,sticky=W)
    label_inscricao_municipal.grid(row=4,column=0,sticky=W)
    entry_inscricao_municipal.grid(row=4,column=1,sticky=W)
    label_cep.grid(row=5,column=0,sticky=W)
    entry_cep.grid(row=5,column=1,sticky=W)
    label_rua.grid(row=6,column=0,sticky=W)
    entry_rua.grid(row=6,column=1,sticky=W)
    label_numero.grid(row=6,column=2,sticky=W)
    entry_numero.grid(row=6,column=3,sticky=W)
    label_complemento.grid(row=6,column=4,sticky=W)
    entry_complemento.grid(row=6,column=5,sticky=W)
    label_bairro.grid(row=7,column=0,sticky=W)
    entry_bairro.grid(row=7,column=1,sticky=W)
    label_municipio.grid(row=7,column=2,sticky=W)
    entry_municipio.grid(row=7,column=3,sticky=W)
    label_uf.grid(row=7,column=4,sticky=W)
    box_uf.grid(row=7,column=5,sticky=W)
    label_telefone.grid(row=8,column=0,sticky=W)
    entry_telefone.grid(row=8,column=1,sticky=W)
    label_celular.grid(row=8,column=3)
    entry_celular.grid(row=8,column=4)
    label_url.grid(row=9,column=0,sticky=W)
    entry_url.grid(row=9,column=1,sticky=W)
    label_email.grid(row=10,column=0,sticky=W)
    entry_email.grid(row=10,column=1,sticky=W)
    button_salvar.grid(row=11,column=4)

    janela_cadastro.mainloop()