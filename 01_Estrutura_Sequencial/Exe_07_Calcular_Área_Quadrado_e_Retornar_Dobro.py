#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#A = b . h
base = int(input('Insira o valor da base do quadrado em cm: ',))
altura = int(input('Insira o valor da altura do quadrado em cm: ',))
a = base * altura ** 2
print(f'A área do quadrado em dobro é {a} cm')