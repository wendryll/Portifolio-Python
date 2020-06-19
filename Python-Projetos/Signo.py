#-*-coding: utf-8-*-
#Código para descobrir o seu signo 

#Variaveis
dia = 0
mes = 0

#programa para descobir o signo de uma pessoa 
def signo(dia,mes):
	if dia >= 20 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 20 and mes == 4:
		print("Signo de Áries!")
	elif dia >= 21 and dia <= 30 and mes == 4 or dia >= 1 and dia <= 20 and mes == 5:
		print("Signo de Touro!")
	elif dia >= 21 and dia <= 31 and mes == 5 or dia >= 1 and dia <= 20 and mes == 6:
		print("Signo de Gêmeos!")
	elif dia >= 21 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 21 and mes == 7:
		print("signo de Câncer!")
	elif dia >= 22 and dia <= 31 and mes == 7 or dia >= 1 and dia <= 22 and mes == 8:
		print("Signo de Leão!")
	elif dia >= 22 and dia <= 31 and mes == 8 or dia >= 1 and dia <= 22 and mes == 9:
		print("Signo de Virgem!")
	elif dia >= 22 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 22 and mes == 10:
		print("Signo de Libra!")
	elif dia  >= 23 and dia <= 31 and mes == 10 or dia >= 1 and dia <= 21 and mes == 11:
		print("Signo de Escorpião")
	elif dia  >= 22 and dia <= 30 and mes == 11 or dia >= 1 and dia <= 21 and mes == 12:
		print("Signo de Sagitário!")
	elif dia  >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 20 and mes == 1:
		print("Signo de Capricórnio!")
	elif dia >= 21 and dia <= 31 and mes == 1 or dia >= 1 and dia <= 18 and mes == 2:
		print("Signo de Aquário!")
	elif dia >= 19 and dia <= 29 and mes == 2 or dia >= 1 and dia <= 19 and mes == 3:
		print("Signo de Peixes!")
	else:
		print("valor invalido!")

#recebendo valores para as variaveis usadas como parametros
dia = int(input('Digite o dia de seu nascimento: '))
mes = int(input('Digite o mes de seu nascimento: '))

#chamando a função
signo(dia,mes)