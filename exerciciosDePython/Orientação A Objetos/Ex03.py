#trabalhando com encapsulamento no python

class Conta:
    def __init__(self,agencia,conta,titular,saldo,corrente=False,poupanca=False):
        self.__agencia = agencia    #atributo privado
        self.__conta = conta        #atributo privado
        self.__titular = titular    #atributo privado
        self.saldo = saldo          
        self.corrente = corrente    
        self.poupanca = poupanca    

    def info(self):
        print('===== Informações da Conta =====')
        print('Agencia: ',self.__agencia)
        print('Conta: ',self.__conta)
        print('Titular: ',self.__titular)
        print('Saldo: R$',self.saldo)
        if self.corrente:
            print('Tipo conta: Corrente')
        elif self.poupanca:
            print("Tipo conta: Poupança")

    def saldoDisponivel(self):
        print('===== Saldo =====')
        print('Saldo: R$',self.saldo)

    def sacar(self,valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo = (self.saldo - valor)
            print('===== Sacar =====')
            print('saldo: R$',self.saldo)
            print('Saque: R$', valor)
            if self.corrente:
                print('Conta: Corrente')
            elif self.poupanca:
                print('Conta: Poupança')

    def deposito(self,valor):
        self.saldo = (self.saldo + valor)
        print('===== Deposito =====')
        print('Deposito: R$',valor)
        print('saldo: R$',self.saldo)
        if self.corrente:
            print('Conta: Corrente')
        elif self.poupanca:
            print('Conta: Poupança')

c1 = Conta(10,1452,"Wendryll",1,False,True)
c1.saldoDisponivel()
