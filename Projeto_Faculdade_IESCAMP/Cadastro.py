from tkinter import *

def Cadastra_cliente():
    #janela
    janela_cadastro = Toplevel()
    janela_cadastro.title =("Cadastro de Clientes")
    #definindo geometria da janela
    largura = 500 #definindo a largura do formulario
    altura = 500  #definido a altura do formulario

    #resolução do nosso sistema
    largura_screen = janela_cadastro.winfo_screenwidth() #retorna o tamanho real da largura do monitor
    altura_screen = janela_cadastro.winfo_screenheight() #retorna o tamanho real da altura do monitor

    #Posição da janela
    posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
    posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

    #definir a geometry
    janela_cadastro.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
    janela_cadastro.resizable(False,False) #definindo que a janela não é redimencionavel
    #widgets
    #frame
    frame_1 = Frame(janela_cadastro,bg='lightblue')
    frame_1.grid(row=0,columnspan=2)
    #Label
    label_razao_social = Label(frame_1, text="Razão Social:",bg='lightblue',font='arial 12') #bg = Background altera a cor de fundo do item
    label_nome_fantasia = Label(frame_1, text="Nome Fantasia:",bg='lightblue',font='arial')
    label_cpnj = Label(frame_1, text="CNPJ:",bg='lightblue',font='arial')
    label_inscricao_estadual = Label(frame_1, text="Inscrição Estadual:",bg='lightblue',font='arial')
    label_inscricao_municipal = Label(frame_1, text="Inscrição Municipal:",bg='lightblue',font='arial')
    label_rua = Label(frame_1, text="Rua:",bg='lightblue',font='arial')
    label_numero = Label(frame_1, text="Número:",bg='lightblue',font='arial')
    label_complemento = Label(frame_1, text="Complemento:",bg='lightblue',font='arial')
    label_bairro = Label(frame_1, text="Bairro:",bg='lightblue',font='arial')
    label_municipio = Label(frame_1, text="Municipio:",bg='lightblue',font='arial')
    label_uf = Label(frame_1, text="UF:",bg='lightblue',font='arial')
    label_cep = Label(frame_1, text="CEP:",bg='lightblue',font='arial')
    label_telefone = Label(frame_1, text="Telefone:",bg='lightblue',font='arial')
    label_whatsapp = Label(frame_1, text="Whatsapp:",bg='lightblue',font='arial')
    label_celular = Label(frame_1, text="Celular:",bg='lightblue',font='arial')
    label_url = Label(frame_1, text="URL:",bg='lightblue',font='arial')
    label_email = Label(frame_1, text="E-mail:",bg='lightblue',font='arial')
    #entry
    entry_razao_social = Entry(frame_1)
    entry_nome_fantasia = Entry(frame_1)
    entry_cpnj = Entry(frame_1)
    entry_inscricao_estadual = Entry(frame_1)
    entry_inscricao_municipal = Entry(frame_1)
    entry_rua = Entry(frame_1)
    entry_numero = Entry(frame_1)
    entry_complemento = Entry(frame_1)
    entry_bairro = Entry(frame_1)
    entry_municipio = Entry(frame_1)
    entry_uf = Entry(frame_1)
    entry_cep = Entry(frame_1)
    entry_telefone = Entry(frame_1)
    entry_whatsapp = Entry(frame_1)
    entry_celular = Entry(frame_1)
    entry_url = Entry(frame_1)
    entry_email = Entry(frame_1)
    #geometria
    label_razao_social.grid(row=0,column=0)
    entry_razao_social.grid(row=0,column=1)
    label_nome_fantasia.grid(row=0,column=0)
    entry_nome_fantasia.grid(row=0,column=1)
    label_cpnj.grid(row=2,column=0)
    entry_cpnj.grid(row=2,column=1)
    label_inscricao_estadual.grid(row=3,column=0)
    entry_inscricao_estadual.grid(row=3,column=1)
    label_inscricao_municipal.grid(row=4,column=0)
    entry_inscricao_municipal.grid(row=4,column=1)
    label_rua.grid(row=5,column=0)
    entry_rua.grid(row=5,column=1)
    label_numero.grid(row=6,column=0)
    entry_numero.grid(row=6,column=1)
    label_complemento.grid(row=7,column=0)
    entry_complemento.grid(row=7,column=1)
    label_bairro.grid(row=8,column=0)
    entry_bairro.grid(row=8,column=1)
    label_municipio.grid(row=9,column=0)
    entry_municipio.grid(row=9,column=1)
    label_uf.grid(row=10,column=0)
    entry_uf.grid(row=10,column=1)
    label_cep.grid(row=11,column=0)
    entry_cep.grid(row=11,column=1)
    label_telefone.grid(row=12,column=0)
    entry_telefone.grid(row=12,column=1)
    label_whatsapp.grid(row=13,column=0)
    entry_whatsapp.grid(row=13,column=1)
    label_celular.grid(row=14,column=0)
    entry_celular.grid(row=14,column=1)
    label_url.grid(row=15,column=0)
    entry_url.grid(row=15,column=1)
    label_email.grid(row=16,column=0)
    entry_email.grid(row=16,column=1)
    #botão
    button_salvar = Button(frame_1, text="Salvar",padx=10)
    #geometria botão
    button_salvar.grid(row=17,column=0)
    janela_cadastro.mainloop()