#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
#18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
# valores para cima, isto é, considere latas cheias.
import math
from typing import Union

m2_por_litro = 6
preco_lata = 80.00
preco_galao = 25.00
litros_lata = 18
litros_galao = 3.6
margem_seguranca = 1.1

m2 = float(input('Informe a quantidade de metros quadrados (m²) a serem pintados: '))

consumo_litro = m2 / m2_por_litro * margem_seguranca

qtd_lata = math.ceil(consumo_litro / litros_lata)
valor_lata = qtd_lata * preco_lata

qtd_galao = math.ceil(consumo_litro / litros_galao)
valor_galao = qtd_galao * preco_galao

qtd_galao_misto = consumo_litro // litros_galao
qtd_lata_misto = math.ceil((consumo_litro - qtd_galao_misto * litros_galao / litros_lata))

valor_lata_misto = qtd_lata_misto * preco_lata
valor_galao_misto = qtd_galao_misto * preco_galao

print(f'A quantidade de latas a serem usadas é {qtd_lata:.0f}, com valor total de R$ {valor_lata}')
print(f'A quantidade de galões a serem usados é {qtd_galao:.0f}, com valor total de R$ {valor_galao}')
print(f'Evitando menor desperdício de tinta temos:')
print(f'Quantidade de latas: {qtd_lata_misto}')
print(f'Quantidade de galões: {qtd_galao_misto}')
print(f'A soma de latas e galões é de : {qtd_lata_misto + qtd_galao_misto}')
print(f'O valor total da soma de latas e galões é de R$ {valor_lata_misto + valor_galao_misto}')