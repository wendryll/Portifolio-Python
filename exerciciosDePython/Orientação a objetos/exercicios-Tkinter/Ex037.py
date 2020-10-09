from tkinter import *

def exit():
    janela.destroy()

#adicionando menus na janela
janela = Tk()#criando objeto tk
janela.geometry("300x200")#dimencionando a janela
meuMenu = Menu(janela) #criando o objeto menu
fileMenu = Menu(meuMenu,tearoff=0) #criando objeto filemenu pertencente ao meuMenu
# tearoff define que o menu não pode ser separado da janela
fileMenu.add_command(label="New")#criando um item do fileMenu
fileMenu.add_command(label='Open')#criando um item do fileMenu
fileMenu.add_command(label='Save')#criando um item do fileMenu
fileMenu.add_separator()#cria uma linha de separação no menu
fileMenu.add_command(label='Exit',command=exit)#passando um evento ao menu por meio do command
meuMenu.add_cascade(label='file',menu=fileMenu)#trasformando o menu em um modelo de cascata
janela.config(menu=meuMenu)#posicionando o menu dentro da janela
janela.mainloop()