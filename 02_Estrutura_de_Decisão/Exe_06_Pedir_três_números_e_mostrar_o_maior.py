#Faça um Programa que leia três números e mostre o maior deles.
primeiro = int(input('Digite o primeiro numero: '))
segundo = int(input('Digite o segundo numero : '))
terceiro = int(input('Digite o terceiro numero: '))

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print(f'O maior número digitado é {maior}')