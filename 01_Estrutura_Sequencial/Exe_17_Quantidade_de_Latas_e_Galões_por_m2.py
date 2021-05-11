#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
#18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
# valores para cima, isto é, considere latas cheias.
import math

m2 = float(input('Insira a área em m² a ser pintada: '))
margem_segurança = 1.1
area_total = m2 * margem_segurança
litros_por_m2 = 6
litros_por_lata = 18
litros_por_galao = 3.6
valor_lata = 80
valor_galao = 25
litros_usados = (m2 * margem_segurança) / litros_por_m2
litros_restantes = litros_usados % litros_por_lata

qtd_apenas_latas = math.ceil(litros_usados / litros_por_lata)
valor_apenas_latas = qtd_apenas_latas * valor_lata
print(f'Você deverá usar {qtd_apenas_latas} latas de 18 litros, no valor de R$ {valor_apenas_latas}')

qtd_apenas_galoes = math.ceil(litros_usados / litros_por_galao)
valor_apenas_galoes = qtd_apenas_galoes * valor_galao
print(f'Você deverá usar {qtd_apenas_galoes} galões de 3.6 litros, no valor de R$ {valor_apenas_galoes}')

qtd_latas = math.floor(litros_usados / litros_por_lata)
preco_lata = qtd_latas * valor_lata

qtd_galoes = math.ceil(litros_restantes / litros_por_galao)
preco_galao = qtd_galoes * valor_galao

preco_total = preco_lata + preco_galao

print(f'Você deverá usar {qtd_latas} de 18 litros mais {qtd_galoes} galões de 3,6 litros, no valor de R$ {preco_total}')



#area_a_ser_pintada = float(input('Insira a área em m² a ser pintada: '))

#area_com_folga = area_a_ser_pintada * 1.1
#litros_por_metro = 6
#qtd_litros_usados = area_com_folga / litros_por_metro

#litros_por_lata = 18
#qtd_latas = math.ceil(qtd_litros_usados / litros_por_lata)
#valor_apenas_latas = qtd_latas * 80

#litros_por_galao = 3.6
#qtd_galoes = math.ceil(qtd_litros_usados / litros_por_galao)
#valor_apenas_galoes = qtd_galoes * 25

#qtd_de_latas = math.floor(qtd_litros_usados / litros_por_lata)
#valor_latas = qtd_de_latas * 80
#litros_restantes = qtd_litros_usados % litros_por_lata
#qtd_de_galoes = math.ceil(litros_restantes / litros_por_galao)
#valor_galoes = qtd_de_galoes * 25

#valor_total = valor_latas + valor_galoes

#print(f'Você deverá usar {qtd_latas} latas de 18 litros, no valor de R$ {valor_apenas_latas}')
#print(f'Você deverá usar {qtd_galoes} galões de 3,6 litros, no valor de R$ {valor_apenas_galoes}')
#print(f'Você deverá usar {qtd_de_latas} de 18 litros mais {qtd_de_galoes} galões de 3,6 litros, no valor de R$ {valor_total}')