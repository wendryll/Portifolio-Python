from tkinter import *
from tkinter import ttk #imoportando o ttk para criar combobox

def mudar_cor(event): #associando o evento do combobox a função
    janela['bg'] = objeto_combobox.get()

janela = Tk()
janela.title('tkinter:combobox')
janela.geometry('250x250')
objeto_combobox = ttk.Combobox(janela)#instanciando um objeto combobox
cores = ("Black","blue","yellow")
objeto_combobox['values'] = cores #atribuindo valores ao combobox
objeto_combobox['state'] = 'disabled' #negando a digitação no campo
objeto_combobox.bind('<<ComboboxSelected>>',mudar_cor)#chamando uma função quando selecioando a opção do combobox
objeto_combobox.pack()
janela.mainloop()