from tkinter import *
#janela que abre outra janela
def executar():
    janela_2 = Tk()
    usuario_label = Label(janela_2,text='usuario:').grid(row=0,column=0)
    senha_label = Label(janela_2,text='senha:').grid(row=1,column=0)
    usuario_text = Entry(janela_2).grid(row=0,column=1)
    senha_text = Entry(janela_2).grid(row=1,column=1)
    bnt = Button(janela_2,text='Logar').grid(column=1)
    janela_2.mainloop()

janela = Tk()
label_1 = Label(janela,text="clique no botão para logar").grid()
bnt = Button(janela,text='clique',command=executar).grid()
janela.mainloop()