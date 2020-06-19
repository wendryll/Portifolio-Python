#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possívies sobre ele.
palavra = input('digite algo: ')

print('O tipo primitivo desse valor é ',type(palavra))
print('Só tem espaços? ',palavra.isspace())
print('É um número? ',palavra.isnumeric())
print('É alfabético? ',palavra.isalpha())
print('É alfanumérico ',palavra.isalnum())
print('ESTÁ em maiúsculas? ',palavra.isupper())
print('ESTÁ em minúsculas? ',palavra.islower())
print('ESTÁ capitalizada? ',palavra.istitle())