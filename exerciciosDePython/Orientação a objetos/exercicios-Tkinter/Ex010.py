from tkinter import *

#alterando label 2

janela = Tk()
janela.title('menu')
msg = Label(janela,text='isto é \n uma mensagem') #criando um label de varias linhas
msg.pack()
msg = Label(text='mensagem 1',bd='10',relief='solid') #usando uma borda solida
msg.pack()
msg = Label(text='mensagem 2',bd='10',relief='flat') #usando uma borda flat
msg.pack()
msg = Label(text='mensagem 3',bd='10',relief='groove') #usando uma borda groove
msg.pack()
msg = Label(text='mensagem 4',bd='10',relief='raised') #usando uma borda raised
msg.pack()
msg = Label(text='mensagem 5',bd='10',relief='sunken') #usando uma borda sunken
msg.pack()
msg = Label(text='mensagem 6',bd='10',relief='ridge') # usando uma borda ridge
msg.pack()
janela.mainloop()