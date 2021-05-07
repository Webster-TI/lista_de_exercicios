#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_horas_trabalhadas = float(input('Insira o valor do seu salário por horas trabalhadas', ))
horas_trabalhadas_mes = float(input('Insira a quantidade de horas trabalhadas no mês', ))
salario_bruto = salario_horas_trabalhadas * horas_trabalhadas_mes
desconto_ir = 0.11 * salario_bruto
desconto_inss = 0.08 * salario_bruto
desconto_sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
print('Confira o seu salário desse mês conforme a tabela abaixo:')
print('Salário Bruto : R$ ', salario_bruto)
print('IR (11%) : R$ ', desconto_ir)
print('INSS (8%) : R$ ', desconto_inss)
print('Sindicato (5%) : R$ ', desconto_sindicato)
print('Salário Líquido : R$ ', salario_liquido)
