from tkinter import *

janela = Tk()
janela.geometry('500x500+100+100')
msg = Label(janela,
            text='justificando texto',
            font='arial 20',
            width='30',
            bd='5',
            relief=SOLID,
            justify=LEFT,
            anchor=W)
msg.pack()
janela.mainloop()