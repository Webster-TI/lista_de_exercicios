# Altere o programa anterior para mostrar no final a soma dos números.

numero_1 = int(input('Digite um número:  '))
numero_2 = int(input('Digite outro número: '))

while numero_1 < numero_2:
    numero_1 = int(input('Digite um número:  '))
    numero_2 = int(input('Digite outro número: '))

else:
	for i in range(numero_1, numero_2,1):
		print(i)