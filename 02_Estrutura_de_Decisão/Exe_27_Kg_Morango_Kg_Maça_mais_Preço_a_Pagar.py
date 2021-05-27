# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = 0
maca = 0
quilos = 0
desconto_10 = 0.10

fruta = int(input('Escolha a fruta que deseja comprar:    1-Morango      2-Maça   '))

if fruta == 1:
    quilos = float(input('Insira a quantidade em Kg de Morango a ser comprada: '))

    if quilos <= 5:
        preco_morango_ate_5_kg = 2.50
        preco_final_morango_ate_5_kg = quilos * preco_morango_ate_5_kg
        print(f'Você está comprando {quilos} Kg de Morango com valor total de R$ {preco_final_morango_ate_5_kg}')

    elif quilos > 5:
        preco_morango_acima_5_kg = 2.20
        preco_final_morango_acima_5_kg = quilos * preco_morango_acima_5_kg
        print(f'Você está comprando {quilos} Kg de Morango com valor total de R$ {preco_final_morango_acima_5_kg}')

    elif quilos > 8 or preco_morango_acima_5_kg > 25:
        preco_morango_acima_8Kg_ou_RS_25 = preco_final_morango_acima_5_kg * desconto_10
        preco_final_morango_acima_8Kg_ou_RS_25 = preco_morango_acima_5_kg - preco_morango_acima_8Kg_ou_RS_25
        print(f'Você está comprando {quilos} Kg de Morango com valor total de R$ {preco_final_morango_acima_8Kg_ou_RS_25}')

if fruta == 2:
    quilos = float(input('Insira a quantidade em Kg de Maça a ser comprada: '))

    if quilos <= 5:
        preco_maca_ate_5_kg = 1.80
        preco_final_maca_ate_5_kg = quilos * preco_maca_ate_5_kg
        print(f'Você está comprando {quilos} Kg de Morango com valor total de R$ {preco_final_maca_ate_5_kg}')

    elif quilos > 5:
        preco_maca_acima_5_kg = 1.50
        preco_final_maca_acima_5_kg = quilos * preco_maca_acima_5_kg
        print(f'Você está comprando {quilos} Kg de Morango com valor total de R$ {preco_final_maca_acima_5_kg}')

    elif quilos > 8 or preco_maca_acima_5_kg > 25:
        preco_maca_acima_8Kg_ou_RS_25 = preco_final_maca_acima_5_kg * desconto_10
        preco_final_maca_acima_8Kg_ou_RS_25 = preco_maca_acima_5_kg - preco_maca_acima_8Kg_ou_RS_25
        print(f'Você está comprando {quilos} Kg de Morango com valor total de R$ {preco_final_maca_acima_8Kg_ou_RS_25}')

continuar = input('Aperte C para continuar comprando:   ')