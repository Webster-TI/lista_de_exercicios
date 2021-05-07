#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#( °C × 9/5) + 32 = °F
c = float(input('Insira a temperatura em graus Celsius: ',))
f = (c * 9/5) + 32
print(f'A temperatura em graus Fahrenheit é {f} F')
