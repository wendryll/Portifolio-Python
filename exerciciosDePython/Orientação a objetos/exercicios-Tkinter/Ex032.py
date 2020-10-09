from tkinter import *

janela = Tk()
janela.geometry("300x200")
slide = Scale(janela,
                from_=0,
                to=100,
                orient=HORIZONTAL,
                resolution=0.5)
slide.pack()
janela.mainloop()