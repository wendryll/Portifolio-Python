from tkinter import *

def apresenta():
    print(valor_check.get())

janela = Tk()
valor_check = IntVar()
check = Checkbutton(janela,text='pressione',variable=valor_check, command=apresenta).grid()
janela.mainloop()