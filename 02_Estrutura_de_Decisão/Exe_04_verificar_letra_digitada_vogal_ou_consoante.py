#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Insira uma letra: ')).upper()

while not letra.isalpha():
    print(f'Por favor, insira uma letra!!! {letra} não é uma letra')
    letter = str(input())

if letra in "aeiou":
    print(f'The letter {letra} é uma vogal')
else:
    print(f'The letter {letra} é uma consoante')