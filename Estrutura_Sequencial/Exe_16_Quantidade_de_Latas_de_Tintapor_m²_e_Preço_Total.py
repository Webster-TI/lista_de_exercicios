#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_para_pintura = float(input('Insira a área em m² a ser pintada: '))
lata_de_tinta = 54
preco_tinta = 80.00
total_de_latas = area_para_pintura / lata_de_tinta
total_preco = total_de_latas * preco_tinta
print(f'Para {area_para_pintura} m², você deverá comprar {total_de_latas} latas e irá pagar R$ {total_preco}.')
