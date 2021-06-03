# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

while True: # Repete até que a condição retornada seja verdadeira.
    try:
        numero = int(input('Insira um valor de 0 a 10: '))
    except ValueError: # Caso o valor seja diferente do solicitado, realizamos o tratamento do erro.
        print('Deve ser fornecido um valor inteiro.')
    else:
        if 0<= numero <= 10: # Dessa forma números negativos não são considerados inteiros válidos.
            print(f'O número informado é {numero}')
            break # Encerra a condição, quando o usuário cumprir o valor solicitado.
        else:
            print('O número deve estar entre 0 e 10.')