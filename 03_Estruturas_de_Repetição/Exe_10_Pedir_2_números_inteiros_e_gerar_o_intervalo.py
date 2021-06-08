# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
# por eles.

numero_1 = int(input('Digite um numero:  '))
numero_2 = int(input('Digite outro numero: '))

while numero_1 < numero_2:
    numero_1 = int(input('Digite um numero:  '))
    numero_2 = int(input('Digite outro numero: '))

else:
	for i in range(numero_1, numero_2,1):
		print(i)