#posicionando elementos na tela por meio do grid
from tkinter import *

janela = Tk()
msg = Label(janela,text='Olá, sejá bem vindo')
msg2 = Label(janela,text='qual seu nome')
msg.grid(row=0,column=0)
msg2.grid(row=1,column=0)
janela.geometry('500x500+200+200')
janela.mainloop()