from tkinter import *

janela = Tk()
janela.geometry('500x500+250+250')
janela.title('menu')
msg = StringVar() #transformando a variavel em um objeto que armazena dados para o tkinter
msg.set("Olá, mundo!") #definindo um valor para está variavel
label1 = Label(janela,textvariable=msg) #chamando a variavel dentro do label
label2 = Label(janela,textvariable=msg)
label1.pack()
label2.pack()
janela.mainloop()