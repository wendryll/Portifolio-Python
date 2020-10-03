#limitando os dados aceitos pelo entry
from tkinter import *
#variaveis
numeros = "0123456789"
def executar(numero):
    valido = numero in numeros
    return valido
    
janela = Tk()
janela.title("4ADS-PA Calcula idade")
#tela

largura = 300 #definindo a largura do formulario
altura = 250  #definido a altura do formulario
#resolução do nosso sistema
largura_screen = janela.winfo_screenwidth() #retorna o tamanho real da largura do monitor
altura_screen = janela.winfo_screenheight() #retorna o tamanho real da altura do monitor
#Posição da janela
posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio
#definir a geometry
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
janela.resizable(False,False)

#widgets
label_nascimento = Label(janela,text='Ano Nascimento?',font='Arial 12',pady=20,width=20)
validando_numero = janela.register(executar)
text_nascimento = Entry(janela,width=15,validate="key",validatecommand=(validando_numero, "%S"))
label_idade1 = Label(janela,text='Idade',font="arial 10")

#layout
label_nascimento.grid(row=0,column=0)
text_nascimento.grid(row=0,column=1)
label_idade1.grid(row=1)

janela.mainloop()