from tkinter import *
#somando numeros
def somar():
    num_1 = int(text_1.get())
    num_2 = int(text_2.get())
    soma = num_1 + num_2
    numero.set(soma)

janela = Tk()
numero = IntVar()
label_1 = Label(janela,text='Entre com um valor: ')
label_2 = Label(janela,text='Entre com outro valor')
Label(janela,textvariable=numero).grid(row=3,column=0)
text_1 = Entry(janela)
text_2 = Entry(janela)
bnt = Button(janela,text='somar',command=somar)
label_1.grid(row=0,column=0)
label_2.grid(row=1,column=0)
text_1.grid(row=0,column=1)
text_2.grid(row=1,column=1)
bnt.grid(row=2,column=1)
janela.mainloop()