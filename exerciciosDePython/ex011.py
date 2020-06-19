#Faça um programa que leia a largura e a altura de uma parede em metros.Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma ára de 2m².

largura = float(input('Digite a Largura da parede: '))
altura = float(input('Digite a Altura da parede: '))
area = largura*altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(area/2))