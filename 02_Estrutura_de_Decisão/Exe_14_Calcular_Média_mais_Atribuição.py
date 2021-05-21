#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
#a sua média. A atribuição de conceitos obedece à tabela abaixo:
  #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0             A
  #Entre 7.5 e 9.0              B
  #Entre 6.0 e 7.5              C
  #Entre 4.0 e 6.0              D
  #Entre 4.0 e zero             E

nota_1 = float(input('Insira o valor da primeira nota: '))
nota_2 = float(input('Insira o valor da segunda nota: '))
media = (nota_1 + nota_2) / 2

if media >= 9.0 and media <= 10.0:
    print(f'A sua média de aproveitamento é de {media} com conceito A')
elif media >= 7.5 and media <= 9.0:
    print(f'A sua média de aproveitamento é de {media} com conceito B')
elif media >= 6.0 and media <= 7.5:
    print(f'A sua média de aproveitamento é de {media} com conceito C')
elif media >= 4.0 and media <= 6.0:
    print(f'A sua média de aproveitamento é de {media} com conceito D')
else:
    print(f'A sua média de aproveitamento é de {media} com conceito E')