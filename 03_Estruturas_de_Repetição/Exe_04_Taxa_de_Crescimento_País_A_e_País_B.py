# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
# a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

populacao_pais_a = 80_000
populacao_pais_b = 200_000
taxa_de_crescimento_pais_a = 1.03
taxa_de_crescimento_pais_b = 1.015
ano = 0

while populacao_pais_a < populacao_pais_b:
    ano += 1
    populacao_pais_a = int(populacao_pais_a * taxa_de_crescimento_pais_a)
    populacao_pais_b = int(populacao_pais_b * taxa_de_crescimento_pais_b)

print(f'População no ano {ano}.')
print(f'População País A: {populacao_pais_a}')
print(f'População País B: {populacao_pais_b}')