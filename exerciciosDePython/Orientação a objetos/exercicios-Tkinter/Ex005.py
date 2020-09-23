#posicionando elementos na janela por meio do pack
from tkinter import *

janela = Tk()
janela.geometry('500x500+200+200')
msg = Label(janela,text='Olá, sejá bem vindo')
msg.pack()
janela.mainloop()