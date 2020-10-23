from tkinter import * #importando biblioteca tkinter
import Cadastro

class MainProgram():
    def __init__(self):
        """
            Espaço reservado para as funções e objetos da classe
        """
        def info():
            info_window = Toplevel()
            info_window.title('Informações da aplicação')
            largura_screen = root.winfo_screenwidth() #retorna o tamanho real da largura do monitor
            altura_screen = root.winfo_screenheight() #retorna o tamanho real da altura do monitor 
            info_conteudo = Listbox(info_window,width=60,bg='lightblue')
            conteudo = ['Desenvolvido por:','João Alves Baldoino Junior RA: 25424','Gustavo Teixeira de Paula RA: 25428',
                        'Manoel Messias dos Santos Junior RA 25402','Thierry Kennedy Coelho da Silva RA: 25331','Wander Massuci RA: 25398','Wendryll Souza Martins RA: 25339']

            for cont in conteudo:
                info_conteudo.insert(END,cont)
            info_conteudo.pack()
            info_window.mainloop()
        """
            Espaço reservado para a criação da janela e suas configurações
        """
        #definindo propriedades da janela
        root = Tk() #criando objeto Tk da biblioteca tkinter
        root.title('ACME - Gerenciamento de clientes')
        #definindo geometria da janela
        largura = 600 #definindo a largura do formulario
        altura =280  #definido a altura do formulario

        #resolução do nosso sistema
        largura_screen = root.winfo_screenwidth() #retorna o tamanho real da largura do monitor
        altura_screen = root.winfo_screenheight() #retorna o tamanho real da altura do monitor

        #Posição da janela
        posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
        posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

        #definir a geometry
        root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
        root.resizable(False,False) #definindo que a janela não é redimencionavel   
        """
            Espaço reservado para a inserção de imagem de plano de fundo no root
        """
        imagem = PhotoImage(file="Projeto_faculdade_IESCAMP/imagem/fundo_root.png")
        root_imagem = Label(root, image=imagem)
        root_imagem.pack()
       
        """
            Espaço reservado para a criação de menus da aplicação
        """
        #Menus da janela
        menu_principal = Menu() #criando objeto da classe menu
        #menu cliente
        clienteMenu = Menu(root,tearoff=0) #criando objeto da classe menu
        clienteMenu.add_command(label='Consultar') #adicionando elementos ao menu
        clienteMenu.add_command(label='Editar') #adicionando elementos ao menu
        clienteMenu.add_command(label='Excluir') #adicionando elementos ao menu
        clienteMenu.add_command(label='cadastrar',command=Cadastro.Cadastra_cliente) #adicionando elementos ao menu
        clienteMenu.add_command(label='Listar') #adicionando elementos ao menu
        menu_principal.add_cascade(menu=clienteMenu,label='Cliente') #transformndo o menu em cascata
        #menu options
        optionsMenu = Menu(root,tearoff=0)
        optionsMenu.add_command(label='Exit',command=root.destroy)#colocando um evento no botão exit do menu
        optionsMenu.add_command(label='Info',command=info)
        menu_principal.add_cascade(menu=optionsMenu,label='Option')
        root.config(menu=menu_principal) #posicionando o menu

        root.mainloop()

    def Exit(self,janela):
        janela.destroy()

janela = MainProgram()