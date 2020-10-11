from tkinter import *

janela = Tk()
janela.geometry('300x200')
spin_1 = Spinbox(janela,from_=0,to=10).pack() #spinbox padrão que vai de 0 a 10
spin_2 = Spinbox(janela,values=(10,20,30,40,50)).pack() #spinbox que aceita apenas os valores passados para o values
spin_3 = Spinbox(janela,values=('anna','breno','joyce','luan','wendryll')).pack() #spinbox que aceita apenas os valores passados para o values
janela.mainloop()