#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
#aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota_1 = float(input('Insira a sua primeira nota: '))
nota_2 = float(input('Insira a sua segunda nota: '))
nota_3 = float(input('Insira a sua terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media == 10:
    print(f'"Aprovado com Distinção" com média de {media}')
elif media >= 7:
    print(f'"Aprovado" com média de {media}')
else:
    print(f'"Reprovado" com média de {media}')