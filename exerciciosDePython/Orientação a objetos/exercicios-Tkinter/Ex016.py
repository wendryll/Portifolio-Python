from tkinter import *
#utilizando columnspan
janela = Tk()
janela.title('menu')
Label(janela,width=40,bg='red').grid(row=0,column=0)
Label(janela,width=40,bg='blue').grid(row=1,column=1)
Label(janela,width=40,bg='green').grid(columnspan=2,sticky='we')
janela.mainloop()