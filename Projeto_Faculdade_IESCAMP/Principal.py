from tkinter import * #importando biblioteca tkinter
import Cadastro
#variaveis globais

root = Tk() #criando objeto tk
root.title('Modulo de vendas')
def encerrar_aplicacao():
    root.destroy()

#Menus da janela
meuMenu = Menu() #criando objeto da classe menu

#menu cliente
clienteMenu = Menu(root,tearoff=0) #criando objeto da classe menu
clienteMenu.add_command(label='Consultar') #adicionando elementos ao menu
clienteMenu.add_command(label='Editar') #adicionando elementos ao menu
clienteMenu.add_command(label='Excluir') #adicionando elementos ao menu
clienteMenu.add_command(label='Inserir',command=Cadastro.Cadastra_cliente) #adicionando elementos ao menu
clienteMenu.add_command(label='Listar') #adicionando elementos ao menu
meuMenu.add_cascade(menu=clienteMenu,label='Cliente') #transformndo o menu em cascata

#menu options
optionsMenu = Menu(root,tearoff=0)
optionsMenu.add_command(label='Exit',command=encerrar_aplicacao)
meuMenu.add_cascade(menu=optionsMenu,label='Option')
root.config(menu=meuMenu) #posicionando o menu

#definindo geometria da janela
largura = 350 #definindo a largura do formulario
altura = 130  #definido a altura do formulario

#resolução do nosso sistema
largura_screen = root.winfo_screenwidth() #retorna o tamanho real da largura do monitor
altura_screen = root.winfo_screenheight() #retorna o tamanho real da altura do monitor

#Posição da janela
posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

#definir a geometry
root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
root.resizable(False,False) #definindo que a janela não é redimencionavel
root.mainloop() #colocando a janela em loop