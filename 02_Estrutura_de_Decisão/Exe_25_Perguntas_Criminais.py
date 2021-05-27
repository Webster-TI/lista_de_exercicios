#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".

print('Responda as perguntas abaixo com "1-SIM" ou "2-NÃO".')

pergunta_1 = int(input('"Telefonou para a vítima?"  '))
pergunta_2 = int(input('"Esteve no local do crime?"  '))
pergunta_3 = int(input('"Mora perto da vítima?"  '))
pergunta_4 = int(input('"Devia para a vítima?"  '))
pergunta_5 = int(input('"Já trabalhou com a vítima?"  '))

respostas_positivas = 0

if pergunta_1 == 1:
    respostas_positivas = respostas_positivas +1
elif pergunta_2 == 1:
    respostas_positivas = respostas_positivas + 1
elif pergunta_3 == 1:
    respostas_positivas = respostas_positivas + 1
elif pergunta_4 == 1:
    respostas_positivas = respostas_positivas + 1
elif pergunta_5 == 1:
    respostas_positivas = respostas_positivas + 1

if respostas_positivas == 2:
    print('Suspeito')
elif respostas_positivas >= 3 or respostas_positivas <= 4:
    print('Cúmplice')
elif respostas_positivas == 5:
    print('Assassino')
else:
    print('Inocente')