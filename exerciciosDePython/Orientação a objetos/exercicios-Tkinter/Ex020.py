from tkinter import *
#exercicio utilizando stringVar
janela = Tk()
janela.title('menu')
#---------------------------------------
def monstrar():
    vartexto.set('O seu nome é ' + text.get())
#---------------------------------------
vartexto = StringVar()
label1 = Label(janela,text='Digite seu nome:')
text = Entry(janela)
bnt = Button(janela,text='Entre',command=monstrar)
label2 = Label(janela,textvariable= vartexto)
#--------------------------------------
label1.grid(row=0,column=0)
text.grid(row=1,column=0)
bnt.grid(row=2,column=0)
label2.grid(row=3,column=0)
janela.mainloop()