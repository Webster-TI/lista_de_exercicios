#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
# os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
# demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

print('Equação do segundo grau ax² + bx + c = 0')

a = int(input('Insira o valor do coeficiente a: '))

if (a == 0):
    print('Essa não é uma egração do segundo grau.')
    print('Programa Encerrado!')
else:
    b = int(input('Insira o valor do coeficiente b: '))
    c = int(input('Insira o valor do coeficiente c: '))
    delta = b * b - (4 * a * c)

    if delta < 0:
        print('Delta é menor que 0, a equação não possui raizes reais.')
        print('Programa Encerrado!')

    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Delta é igual a 0, possui apenas uma raiz real {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Delta é maior que 0 e possui as raizes {raiz1} e {raiz2}')