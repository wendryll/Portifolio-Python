from tkinter import *

def exibir():
    nomeCompleto = text_nome.get() + " " + text_sobrenome.get() 
    label_vazio['text'] = nomeCompleto

def cancelar():
    janela.destroy()#fecha a janela

janela = Tk()
janela.geometry("400x200+350+200")
#label
label_nome = Label(janela,text='Nome',pady=7)
label_sobrenome = Label(janela,text='Sobrenome:',pady=7)
label_nomecompleto = Label(janela,text='Nome Completo',pady=7)
label_vazio = Label(janela,text='',pady=10)
#entry
text_nome = Entry(janela,width=30)
text_sobrenome = Entry(janela,width=30)
#batão
bnt_mostrar = Button(janela,text='Mostrar',command=exibir)
bnt_cancelar = Button(janela,text='Cancelar',command=cancelar)
#layout
label_nome.grid(row=0,column=0)
label_sobrenome.grid(row=1,column=0)
label_nomecompleto.grid(row=2,column=0)
label_vazio.grid(row=2,column=1)
text_nome.grid(row=0,column=1)
text_sobrenome.grid(row=1,column=1)
bnt_cancelar.grid(row=3,column=1)
bnt_mostrar.grid(row=3,column=0)
janela.mainloop()
