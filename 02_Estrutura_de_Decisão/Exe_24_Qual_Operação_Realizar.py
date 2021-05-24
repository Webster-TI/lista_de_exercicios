#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

numero_1 = float(input('Insira o valor do primeiro número: '))
numero_2 = float(input('Insira o valor do segundo número: '))

print('1-Adição     2-Subtração     3-Divisão       4-Multiplicação')
opcao = int(input('Escolha qual operação quer realizar: '))

if opcao == 1:
    resultado = numero_1 + numero_2
elif opcao == 2:
    resultado = numero_1 - numero_2
elif opcao == 3:
    resultado = numero_1 / numero_2
elif opcao == 4:
    resultado = numero_1 * numero_2
else:
    print('Opção Inválida!!')

if resultado % 2 == 0:
    print(f'O número {resultado} é par.')
else:
    print(f'O número {resultado} é impar.')

if resultado > 0:
    print(f'O número {resultado} é positivo.')
else:
    print(f'O número {resultado} é negativo.')

if resultado == round(resultado):
    print(f'O número {resultado} é inteiro.')
else:
    print(f'O número {resultado} é decimal.')
