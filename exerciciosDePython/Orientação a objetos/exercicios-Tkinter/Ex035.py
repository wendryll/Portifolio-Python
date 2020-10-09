from tkinter import *
from datetime import date
def calcular():
    idade = date.today().year - int(text_nascimento.get()) #obtendo e convertendo o ano para idade
    label_vazio['text'] = idade #atribuindo os valores ao label

def cancelar():
    janela.destroy() #fechando a janela
#objetos
janela = Tk()
label_nascimento = Label(janela,text='Ano nascimento?')
text_nascimento = Entry(janela)
label_idade = Label(janela,text='Idade')
label_vazio = Label(janela)
bnt_calcular = Button(janela,text='calcular',command=calcular)
bnt_cancelar = Button(janela,text='cancelar',command=cancelar)
#layout
label_nascimento.grid(row=0,column=0)
text_nascimento.grid(row=0,column=1)
label_idade.grid(row=2,column=0)
label_vazio.grid(row=2,column=1)
bnt_calcular.grid(row=3,column=1)
bnt_cancelar.grid(row=3,column=2)

janela.mainloop()
