from tkinter import *

janela = Tk()
janela.title('Login')
Label(janela,text='usuario: ').grid(row=0,column=0,sticky=W) #label statico ao qual não é alteravel
Label(janela,text='senha: ').grid(row=1,column=0,sticky=W)#label statico ao qual não é alteravel

textbox1 = Entry(janela).grid(row=0,column=1)
textbox2 = Entry(janela).grid(row=1,column=1)

bnt = Button(janela,text='Entre').grid(row=2,column=1,sticky=E)
janela.mainloop()