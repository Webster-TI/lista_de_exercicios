# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
# entrada e permita repetir a operação.

populacao_pais_a = int(input('Insira o valor da população do país A: '))
while populacao_pais_a <= 0:
    populacao_pais_a = int(input('A população deve ser maior que zero: '))

taxa_de_crescimento_pais_a = float(input('Insira a taxa de crescimento do país A: '))
while taxa_de_crescimento_pais_a <= 0:
    taxa_de_crescimento_pais_a = float(input('A taxa de crescimento deve ser maior que zero: '))

populacao_pais_b = int(input('Insira o valor da população do país B: '))
while populacao_pais_b <= 0:
    populacao_pais_b = int(input('A população deve ser maior que zero: '))

taxa_de_crescimento_pais_b = float(input('Insira a taxa de crescimento do país B: '))
while taxa_de_crescimento_pais_b <= 0:
    taxa_de_crescimento_pais_b = float(input('A taxa de crescimento deve ser maior que zero: '))

ano = 0

while populacao_pais_a < populacao_pais_b:
    ano += 1
    populacao_pais_a = int(populacao_pais_a * taxa_de_crescimento_pais_a)
    populacao_pais_b = int(populacao_pais_b * taxa_de_crescimento_pais_b)

print(f'População no ano {ano}.')
print(f'População País A: {populacao_pais_a}')
print(f'População País B: {populacao_pais_b}')
