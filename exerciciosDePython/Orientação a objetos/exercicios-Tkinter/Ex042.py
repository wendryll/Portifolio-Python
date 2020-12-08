from tkinter import *
from tkinter import ttk

janela_teste = Tk()
janela_teste.title("4ADS-PA | Apresenta o mês")

maiusculo = IntVar()

label_mes = Label(janela_teste,text="Mês").grid(row=0,column=0,sticky=W)

lista_mes = ttk.Combobox(janela_teste)
mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
lista_mes['value'] = mes
lista_mes['state'] = 'readonly'
lista_mes.current(10)
lista_mes.grid(row=0,column=1,sticky=W)

label_mes_extenso = Label(janela_teste,text='Mês por Extenso').grid(row=1,column=0,sticky=W)
label_exibe = Label(janela_teste,text='')
label_exibe.grid(row=1,column=1,sticky=W)
def upper():
    label_exibe['text'] = lista_mes.get().upper()

def mostrar():
    label_exibe['text'] = lista_mes.get()

def exit():
    janela_teste.destroy()

checkbutton = Checkbutton(text='Maíusculo',variable=maiusculo,command=upper).grid(row=2,column=2,sticky=W)

button_mostrar = Button(text='mostrar', command=mostrar).grid(row=3,column=1,sticky=W)
button_cancelar = Button(text='cancelar',command=exit).grid(row=3,column=2,sticky=W)
janela_teste.mainloop()