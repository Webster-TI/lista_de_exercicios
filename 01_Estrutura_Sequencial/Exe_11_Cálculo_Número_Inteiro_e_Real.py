#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    #o produto do dobro do primeiro com metade do segundo .
    #a soma do triplo do primeiro com o terceiro.
    #o terceiro elevado ao cubo.
n1 = int(input('Insira o valor do primeiro número inteiro: '))
n2 = int(input('Insira o valor do segundo número inteiro: '))
n_real = float(input('Insira o valor do número real: '))
r1 = n1 * 2 * (n2 / 2)
r2 = n1 * 3 + n_real
r3 = n_real ** 2
print(f'O produto do dobro do primeiro com metade do segundo é: {r1}')
print(f'A soma do triplo do primeiro com o terceiro é: {r2}')
print(f'O terceiro elevado ao cubo é: {r3}')