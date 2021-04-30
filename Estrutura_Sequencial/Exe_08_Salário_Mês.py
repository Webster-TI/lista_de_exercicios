#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# #Calcule e mostre o total do seu salário no referido mês.
salario_hora_trabalhada = float(input('Insira o seu salário ganho por hora trabalhada: '))
horas_trabalhadas_mes = float(input('Insira a quantidade de horas trabalhadas no mês: '))
salario_bruto = salario_hora_trabalhada * horas_trabalhadas_mes
print(f'Você recebeu R$ {salario_bruto} este mês')