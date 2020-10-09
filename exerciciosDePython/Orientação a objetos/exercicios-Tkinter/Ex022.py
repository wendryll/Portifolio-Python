from tkinter import *
#mexer
janela = Tk()
janela.title('menu')
lista = Listbox(janela)
lista.insert(END,"maçã")
lista.insert(END,'uva')
lista.insert(END,'banana')
lista.pack()
janela.mainloop()