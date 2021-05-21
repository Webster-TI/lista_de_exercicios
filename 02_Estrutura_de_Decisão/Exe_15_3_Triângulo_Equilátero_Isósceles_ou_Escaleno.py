#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado_a = float(input('Insira o valor do lado A do triângulo: '))
lado_b = float(input('Insira o valor do lado B do triângulo: '))
lado_c = float(input('Insira o valor do lado C do triângulo: '))

if lado_a == lado_b == lado_c:
    print('Esse é Triângulo Equilátero')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print('Esse é um Triângulo Isósceles')
elif lado_a != lado_b and lado_c:
    print('Esse é um Triângulo Escaleno')