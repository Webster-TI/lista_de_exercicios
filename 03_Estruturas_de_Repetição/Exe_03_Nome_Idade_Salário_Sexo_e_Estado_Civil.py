# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Insira o seu nome (Maior que 3 caracteres): '))
while len(nome) <= 3:
    nome = input('Seu nome deve conter mais de 3 caracteres: ')

idade = int(input('Insira a sua idade (Entre 0 e 150): '))
while idade < 0 or idade > 150:
    idade = input('Sua idade deve estar entre 0 e 150: ')

salario = float(input('Insira o seu salário (Maior que zero): '))
while salario <0:
    salario = input('Seu salário deve ser maior que zero: ')

sexo = str(input('Insira o seu sexo: "f-Feminino"   "m-Masculino"   '))
while sexo != 'f' and sexo != 'm':
    sexo = input('Seu sexo deve ser "f" ou "m": ')

estado_civil = str(input('Insira o seu estado cicil: "s-Solteiro"   "c-Casado"  v-Viúvo"    "d-Divorciado": '))
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Insira o seu estado cicil: "s-Solteiro"   "c-Casado"  v-Viúvo"    "d-Divorciado": ')
