from tkinter import *
#utilizando toplevel
janela = Tk()
#toplevel
def janela_superior():
    janela_1 = Toplevel() #criando uma janela toplevel
    Label(janela_1,text='sou um toplevel').pack()
    janela_1.mainloop()


janela.geometry("300x200")
bnt = Button(janela,text='entre',command=janela_superior).pack()
janela.mainloop()