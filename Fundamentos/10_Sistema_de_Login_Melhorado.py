print("Bem-Vindo ao nosso sistema, por favor, faça o login para continuar! ")
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

while usuario != "Peter Parker" or senha != "Obaranha":
    print("Usuario ou senha incorretos, tente novamente! ")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

print("Login realizado com sucesso! ")