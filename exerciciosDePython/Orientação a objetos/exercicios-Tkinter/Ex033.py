#RadioButton
from tkinter import *

janela = Tk()
janela.geometry("200x100")
variavel_a = IntVar()
frame_1 = Frame(janela).pack()
label_1 = Label(frame_1,text='Sexo:').pack()
bnt_1 = Radiobutton(janela,text='Masculino',variable=variavel_a,value=1)
bnt_2 = Radiobutton(janela,text='Feminino',variable=variavel_a,value=2)
bnt_3 = Button(frame_1,text='confirmar')
bnt_1.pack()
bnt_2.pack()
bnt_3.pack()
bnt_1.select()

janela.mainloop() 