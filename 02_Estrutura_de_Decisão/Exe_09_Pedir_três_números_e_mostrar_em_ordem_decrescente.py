# Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = []
qtd_de_itens_da_lista = 3
for i in range(qtd_de_itens_da_lista):
    elemento = int(input('Digite um numero: '))
    lista.append(elemento)

lista.sort(reverse = True) #ordena os elementos
print(lista)
