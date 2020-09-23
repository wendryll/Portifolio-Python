from tkinter import *   
#exercicio janela que calcula FAHRENHEIT PARA CELSIUS
def calcular():
    F = float(text.get()) #usar get apenas em Entry()
    C = (F-32) * 5/9
    final.set(str(C) + 'grus celsius')
janela = Tk()
janela.title('conversor')

final = StringVar()

frame_conversor = Frame(janela)
label = Label(frame_conversor,text='FAHRENHEIT:')
text = Entry(frame_conversor)
label2 = Label(frame_conversor,textvariable=final)
bnt = Button(frame_conversor,text='confirmar',command=calcular)

label.grid(row=0,column=0)
text.grid(row=1,column=0)
bnt.grid(row=2,column=0)
label2.grid(row=3,column=0)
frame_conversor.grid()
janela.mainloop()