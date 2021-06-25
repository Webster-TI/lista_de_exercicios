# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

base = (int(input('Insira o valor da base: ')))
expoente = (int(input('Insira o valor da expoente: ')))

potencia = 1

for i in range(expoente):
    potencia *= base
    i += 1

print(f'{base} elevado a {expoente} é igual a {potencia}.')