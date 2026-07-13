print("=== Sistema de Cadastro de Usuários ===")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")

while nome == "" or email == "" or senha == "":
    print("Todos os campos são obrigatórios, por favor, preencha todos os campos! ")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

print("Cadastro realizado com sucesso! ")