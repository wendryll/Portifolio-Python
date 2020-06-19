#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando umaa mensagem no final, de acordo com a média atingida Média abaixo de 5 reprovado, Média entre 5 e 6.9 recuperação, Média 7 ou superior  Aprovado

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1+nota2)/2

if media < 5:
    print('O aluno teve a Média {:.1f} e está reprovado'.format(media))
elif media >= 5 and media <= 6.9 :
    print('O aluno teve a Média {:.1f} e está em recuperação'.format(media))
elif media >= 7 and media <= 10:
    print('O aluno teve a Média {:.1f} e está aprovado'.format(media))
else:
    print('Alguma nota foi digitada errada!')