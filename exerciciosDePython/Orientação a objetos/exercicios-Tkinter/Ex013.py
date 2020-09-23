from tkinter import *

#trabalhando com posicionamentos de objetos por meio do grid 

janela = Tk()
janela.geometry('500x500+250+250')
label1 = Label(text='mensagem 1',font="Arial 20",bg='red')
label2 = Label(text='mensagem 2',font='Arial 20',bg='green')
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
janela.mainloop()