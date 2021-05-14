#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

produto_1 = float(input('Insira o valor do primeiro produto: '))
produto_2 = float(input('Insira o valor do segundo produto: '))
produto_3 = float(input('Insira o valor do terceiro produto: '))

menor_preco = produto_1
produto_para_comprar = menor_preco

if produto_2 < menor_preco:
    menor_preco = produto_2
elif produto_3 < menor_preco:
    menor_preco = produto_3

print(f'O melhor produto para comprar está com o menor valor de R$ {menor_preco}')