#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
#quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
#mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na
#máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e
#uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
#uma nota de 5 e quatro notas de 1.

print('O valor mínimo para saque é de R$ 10,00')
print('O valor máximo para saque é de R$ 600,00')

print( 'Notas disponíveis R$ 1, R$ 5, R$ 10, R$ 50 e R$ 100')

saque = int(input('Insira o valor que deseja sacar: '))

notas_100_str = notas_50_str = notas_10_str = notas_5_str = notas_1_str = ''

notas_100 = int(saque / 100)
saque = saque % 100

notas_50 = int(saque / 50)
saque = saque % 50

notas_10 = int(saque / 10)
saque = saque % 10

notas_5 = int(saque / 5)
saque = saque % 5

notas_1 = saque

print(f'Você está sacando {notas_100} notas de R$ 100, {notas_50} notas de R$ 50, {notas_10} notas de R$ 10, {notas_5} '
      f'notas de R$ 5 e {notas_1} notas de R$ 1.')