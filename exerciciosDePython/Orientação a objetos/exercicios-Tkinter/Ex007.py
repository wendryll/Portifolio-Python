#associando um evento ao botão
from tkinter import *

def mensagem():
    print('Olá, mundo!') #tera uma saida no console

janela = Tk()
janela.title('Janela')
janela.geometry('250x250+400+400')
bnt = Button(janela,text='Executar',command=mensagem)
bnt.pack()
janela.mainloop()