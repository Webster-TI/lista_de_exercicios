#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura_homem = float(input('Insira a altura do homem: '))
altura_mulher = float(input('Insira a altura da mulher: '))
peso_ideal_homem = (72.7 * altura_homem) - 58
peso_ideal_mulher = (62.1 * altura_mulher) - 44.7
print(f'O peso ideal para homens com base na altura informada é {peso_ideal_homem} kg')
print(f'O peso ideal para mulheres com base na altura informada é {peso_ideal_mulher} kg')