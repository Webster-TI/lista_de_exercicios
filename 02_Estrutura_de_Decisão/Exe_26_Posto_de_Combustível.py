#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro

# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos,o tipo de combustível (codificado da seguinte
# forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
# gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

alcool = 0
gasolina = 0

preco_alcool = 1.90
preco_gasolina = 2.50

desconto_ate_20_litros_alcool = 0.03
desconto_acima_20_litros_alcool = 0.05

desconto_ate_20_litros_gasolina = 0.04
desconto_acima_20_litros_gasolina = 0.06

opcao = str(input('Escolha o combustível a ser abastecido:  A-álcool  ou  G-gasolina:  '))

if opcao == 'A' or opcao == 'a':
    alcool = int(input('Insira a quantidade de álcool para abastecer: '))
    if alcool <= 20:
        preco_litro_alcool_ate_20_litros = alcool * preco_alcool
        preco_desconto_ate_20_litros_alcool = preco_litro_alcool_ate_20_litros * desconto_ate_20_litros_alcool
        preco_final_ate_20_litros_alcool = preco_litro_alcool_ate_20_litros - preco_desconto_ate_20_litros_alcool
        print(f'Voce está abastecendo {alcool} litros de Álcool com valor total de R$ {preco_final_ate_20_litros_alcool}')
    elif alcool > 20:
        preco_litro_alcool_acima_20_litros = alcool * preco_alcool
        preco_desconto_acima_20_litros_alcool = preco_litro_alcool_acima_20_litros * desconto_acima_20_litros_alcool
        preco_final_acima_20_litros_alcool = preco_litro_alcool_acima_20_litros - preco_desconto_acima_20_litros_alcool
        print(
            f'Voce está abastecendo {alcool} litros de Álcool com valor total de R$ {preco_final_acima_20_litros_alcool}')

if opcao == 'G' or opcao == 'g':
    gasolina = int(input('Insira a quantidade de gasolina para abastecer: '))
    if gasolina <= 20:
        preco_litro_gasolina_ate_20_litros = gasolina * preco_gasolina
        preco_desconto_ate_20_litros_gasolina = preco_litro_gasolina_ate_20_litros * desconto_ate_20_litros_gasolina
        preco_final_ate_20_litros_gasolina = preco_litro_gasolina_ate_20_litros - preco_desconto_ate_20_litros_gasolina
        print(f'Voce está abastecendo {gasolina} litros de Gasolina com valor total de R$ {preco_final_ate_20_litros_gasolina}')
    elif alcool > 20:
        preco_litro_alcool_acima_20_litros = gasolina * preco_gasolina
        preco_desconto_acima_20_litros_gasolina = preco_litro_gasolina_acima_20_litros * desconto_acima_20_litros_gasolina
        preco_final_acima_20_litros_gasolina = preco_litro_gasolina_acima_20_litros - preco_desconto_acima_20_litros_gasolina
        print(
            f'Voce está abastecendo {gasolina} litros de Gasolina com valor total de R$ {preco_final_acima_20_litros_gasolina}')