#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
# o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input('Insira o valor do salário para reajuste: '))
aumento_percentual_20 = 0.20
aumento_percentual_15 = 0.15
aumento_percentual_10 = 0.10
aumento_percentual_05 = 0.05

if salario == 280:
    aumento_percentual = salario * aumento_percentual_20
    salario_ajustado = salario + aumento_percentual
    print(f'O seu salário é de R$ {salario}')
    print(f'O percentual de aumento aplicado foi de 20%')
    print(f'O valor do aumento é de R$ {aumento_percentual}')
    print(f'O novo salário após o aumento é de R$ {salario_ajustado}')

elif salario >= 281 and salario <= 700:
    aumento_percentual = salario * aumento_percentual_15
    salario_ajustado = salario + aumento_percentual
    print(f'O seu salário é de R$ {salario}')
    print(f'O percentual de aumento aplicado foi de 15%')
    print(f'O valor do aumento é de R$ {aumento_percentual}')
    print(f'O novo salário após o aumento é de R$ {salario_ajustado}')

elif salario >= 701 and salario <= 1500:
    aumento_percentual = salario * aumento_percentual_10
    salario_ajustado = salario + aumento_percentual
    print(f'O seu salário é de R$ {salario}')
    print(f'O percentual de aumento aplicado foi de 10%')
    print(f'O valor do aumento é de R$ {aumento_percentual}')
    print(f'O novo salário após o aumento é de R$ {salario_ajustado}')

else:
    aumento_percentual = salario * aumento_percentual_05
    salario_ajustado = salario + aumento_percentual
    print(f'O seu salário é de R$ {salario}')
    print(f'O percentual de aumento aplicado foi de 5%')
    print(f'O valor do aumento é de R$ {aumento_percentual}')
    print(f'O novo salário após o aumento é de R$ {salario_ajustado}')
