#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
# os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

salario_horas_trabalhadas = float(input('Insira o valor do seu salário por horas trabalhadas: ', ))
horas_trabalhadas_mes = int(input('Insira a quantidade de horas trabalhadas no mês: ', ))
salario_bruto = salario_horas_trabalhadas * horas_trabalhadas_mes
ir_05 = 0.05
ir_10 = 0.10
ir_20 = 0.20
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    print(f'Salário Bruto:      :R$ {salario_bruto}')
    print(f'(-)  IR (5%)        :R$ ISENTO')
    print(f'(-) INSS (10%)      :R$ {inss}')
    print(f'FGTS (11%)          :R$ {fgts}')
    print(f'Total de descontos  :R$ {total_de_descontos}')
    print(f'Salário Liquido     :R$ {salario_bruto - inss}')

if salario_bruto >= 901 and salario_bruto <= 1500:
    ir = salario_bruto * ir_05
    total_de_descontos = ir + inss
    salario_liquido = salario_bruto - total_de_descontos
    print(f'Salário Bruto:      :R$ {salario_bruto}')
    print(f'(-)  IR (5%)        :R$ {ir}')
    print(f'(-) INSS (10%)      :R$ {inss}')
    print(f'FGTS (11%)          :R$ {fgts}')
    print(f'Total de descontos  :R$ {total_de_descontos}')
    print(f'Salário Liquido     :R$ {salario_liquido}')

if salario_bruto >= 1501 and salario_bruto <= 2500:
    ir = salario_bruto * ir_10
    total_de_descontos = ir + inss
    salario_liquido = salario_bruto - total_de_descontos
    print(f'Salário Bruto:      :R$ {salario_bruto}')
    print(f'(-)  IR (10%)       :R$ {ir}')
    print(f'(-) INSS (10%)      :R$ {inss}')
    print(f'FGTS (11%)          :R$ {fgts}')
    print(f'Total de descontos  :R$ {total_de_descontos}')
    print(f'Salário Liquido     :R$ {salario_liquido}')

else:
    ir = salario_bruto * ir_20
    total_de_descontos = ir + inss
    salario_liquido = salario_bruto - total_de_descontos
    print(f'Salário Bruto:      :R$ {salario_bruto}')
    print(f'(-)  IR (20%)        :R$ {ir}')
    print(f'(-) INSS (10%)      :R$ {inss}')
    print(f'FGTS (11%)          :R$ {fgts}')
    print(f'Total de descontos  :R$ {total_de_descontos}')
    print(f'Salário Liquido     :R$ {salario_liquido}')