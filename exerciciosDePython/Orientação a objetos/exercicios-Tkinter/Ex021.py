from tkinter import *
#PEQUENO EXERCÍCIO COM WIDGETS E EVENTOS

#DEF
#--------------------------------------
def mostrar():
    """
        -> está função cria um label que apresenta o nome do usuario ao final da janela.
    """
    nome = text_1.get()
    label_final = Label(janela,text='O seu nome é ' + nome)
    label_final.grid()

#GUI
#--------------------------------------
janela = Tk()
janela.title('menu')
janela.geometry('150x100')
#--------------------------------------
#widgets
label_1 = Label(janela,text='Qual seu nome')
text_1 = Entry(janela)
bnt_1 = Button(janela,text='Entre',command=mostrar)
#Posicionamento
label_1.grid()
text_1.grid()
bnt_1.grid()

janela.mainloop()