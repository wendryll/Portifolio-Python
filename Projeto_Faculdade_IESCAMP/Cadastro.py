from tkinter import * #importando a biblioteca tkinter
from tkinter import ttk #importando ttk para criação do combobox
import DadosValidacao #importando arquivo com as variaveis de validação
import mysql.connector #importando o conector com o banco de dados SQL
#banco de dados
db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="vendas") #conecta com a base de dados
cursor = db_connection.cursor() #vai executar os comandos SQL


#funções
def possui():
    pass

def salvar():
    pass

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
    valido = i in DadosValidacao.letras + DadosValidacao.numeros + DadosValidacao.simbolo_email
    return valido

def validar_url(i):
    """
    ->validar_url:
        -parametro i corresponde a qualquer coisa digitada pelo usuario
        -funcao que verifica se o que foi digitado pelo usuario esta contido dentro das variaveis, numeros, letras, simbolo_url,
        em caso afirmativo o valor é devolvido, caso contrario o valor nao é devolvido
    """
    valido = i in DadosValidacao.letras + DadosValidacao.numeros + DadosValidacao.simbolo_url
    return valido

def validar_letra_numero(i):
    """
    -parametro i corresponde a qualquer coisa digitada pelo usuario
        -funcao que verifica se o que foi digitado pelo usuario esta contido dentro da variaveis, numeros, letras,
        em caso afirmativo o valor é devolvido, caso contrario o valor nao é devolvido
    """
    valido = i in DadosValidacao.letras + DadosValidacao.numeros
    return valido

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
    label_razao_social = Label(janela_cadastro, text="Razão Social:",font='arial')
    label_nome_fantasia = Label(janela_cadastro, text="Nome Fantasia:",font='arial')
    label_cnpj = Label(janela_cadastro, text="CNPJ:",font='arial')
    label_inscricao_estadual = Label(janela_cadastro, text="Inscrição Estadual:",font='arial')
    label_inscricao_municipal = Label(janela_cadastro, text="Inscrição Municipal:",font='arial')
    label_rua = Label(janela_cadastro, text="Rua:",font='arial')
    label_numero = Label(janela_cadastro, text="Número:",font='arial')
    label_complemento = Label(janela_cadastro, text="Complemento:",font='arial')
    label_bairro = Label(janela_cadastro, text="Bairro:",font='arial')
    label_municipio = Label(janela_cadastro, text="Municipio:",font='arial')
    label_uf = Label(janela_cadastro, text="UF:",font='arial')
    label_cep = Label(janela_cadastro, text="CEP:",font='arial')
    label_telefone = Label(janela_cadastro, text="Telefone:",font='arial')
    label_celular = Label(janela_cadastro,text="Celular:",font='arial')
    label_url = Label(janela_cadastro, text="URL:",font='arial')
    label_email = Label(janela_cadastro, text="E-mail:",font='arial')
    """
        Espaço reservado para a criação de entrys(tkinters)
    """
    entry_razao_social = Entry(janela_cadastro,width=80)
    entry_nome_fantasia = Entry(janela_cadastro,width=80)
    entry_cnpj = Entry(janela_cadastro,validate='key',validatecommand=(validando_numero,"%S"),width=15)
    entry_inscricao_estadual = Entry(janela_cadastro,validate='key',validatecommand=(validando_numero,"%S"),width=40)
    entry_inscricao_municipal = Entry(janela_cadastro,validate='key',validatecommand=(validando_numero,"%S"),width=40)
    entry_rua = Entry(janela_cadastro,width=40,validate="key",validatecommand=(validar_letra_numero,"%S"))
    entry_numero = Entry(janela_cadastro,validate='key',validatecommand=(validando_numero,"%S"),width=10)
    entry_complemento = Entry(janela_cadastro,width=20,validate="key",validatecommand=(validar_letra_numero,"%S"))
    entry_bairro = Entry(janela_cadastro,width=20,validate="key",validatecommand=(validar_letra_numero,"%S"))
    entry_municipio = Entry(janela_cadastro,width=40,validate="key",validatecommand=(validar_letra_numero,"%S"))
    entry_cep = Entry(janela_cadastro,validate='key',validatecommand=(validando_numero,"%S"),width=13)
    entry_telefone = Entry(janela_cadastro,validate='key',validatecommand=(validando_numero,"%S"),width=13)
    entry_celular = Entry(janela_cadastro,validate='key',validatecommand=(validando_numero,"%S"),width=13)
    entry_url = Entry(janela_cadastro,width=40,validate='key',validatecommand=(validando_url,"%S"))
    entry_email = Entry(janela_cadastro,validate='key',validatecommand=(validando_email,"%S"),width=40)
    """
        Espaço reservado para a criação de checkbutton(tkinter)
    """
    bnt_whatsapp = Checkbutton(janela_cadastro,text="Whatsapp:",variable=valor_whatsapp).grid(row=8,column=5)

    """
        Espaço reservado para a criação de button(tkinter)
    """
    button_salvar = Button(janela_cadastro, text="Salvar",command=salvar)

    #combobox
    """
        Espaço reservado para a criação de um combobox que busca os dados dentro de uma tabela da base de dados para 
        a exibição ao usuario.
    """
    box_uf = ttk.Combobox(janela_cadastro)#instanciando o objeto combobox
    box_uf['state'] = 'readonly' #deixando o compo sem digitação para o usuario
    cursor.execute('SELECT uf FROM uf') #comando select do MySQL
    myresult = cursor.fetchall()
    lista_uf = [] #lista com uf de uma tabela do banco de dados
    for i in myresult:      #for que percorre o conteudo da tabela uf do banco de dados
        lista_uf.append(i)  #adicionando o conteudo da tabela dentro de uma lista
    box_uf['values'] = lista_uf #atribuindo a lista ao combobox

    #geometria
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