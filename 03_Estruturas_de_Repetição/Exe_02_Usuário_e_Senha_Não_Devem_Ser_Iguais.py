# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.

while True:
    try:
        usuario = str(input('Insira o seu nome de usuário: '))
        senha = str(input('Insira a sua senha: '))
    except ValueError:
        print('Deve ser inserido um usuário e senha diferentes.')
    else:
        if usuario == senha:
            print('A senha não pode ser igual ao usuário!!')
        elif usuario != senha:
            print('Usuário e Senha estão diferentes, login aceito!')
            break
