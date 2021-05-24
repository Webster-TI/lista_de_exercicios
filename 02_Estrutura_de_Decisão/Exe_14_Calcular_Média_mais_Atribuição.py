#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
#a sua média. A atribuição de conceitos obedece à tabela abaixo:
  #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0             A
  #Entre 7.5 e 9.0              B
  #Entre 6.0 e 7.5              C
  #Entre 4.0 e 6.0              D
  #Entre 4.0 e zero             E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
#A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota_1 = float(input('Insira o valor da primeira nota: '))
nota_2 = float(input('Insira o valor da segunda nota: '))
media = (nota_1 + nota_2) / 2

if media >= 9.0 and media <= 10.0:
    conceito = 'A'
elif media >= 7.5 and media <= 9.0:
    conceito = 'B'
elif media >= 6.0 and media <= 7.5:
    conceito = 'C'
elif media >= 4.0 and media <= 6.0:
    conceito = 'D'
else:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    resultado = 'APROVADO'
else:
    resultado = 'REPROVADO'

print(f'Sua primeira nota foi {nota_1}')
print(f'Sua segunda nota foi {nota_2}')
print(f'A sua média foi de {media}')
print(f'O seu conceito foi {conceito}')
print(f'Você foi "{resultado}".')