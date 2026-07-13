print("==== Bem-vindo ao Mercadinho online! ==== ")
total_da_compra = float(0.00)
opcao= input("lista de produtos: 1 - Arroz (R$ 25.00) , 2 - Feijão (R$ 19.50), 3 - Macarrão (R$ 15.60), 4 - Óleo (R$ 10.00), 5 - Açúcar (R$ 10.00), 6 - Finalizar compra. Digite o número do produto que deseja comprar: ")

while opcao != "6":
    if opcao == "1": 
        print("Você adicionou Arroz ao carrinho! ")
        total_da_compra += 25.00
    elif opcao == "2":
        print("Você adicionou Feijão ao carrinho! ")
        total_da_compra += 19.50
    elif opcao == "3":
        print("Você adicionou Macarrão ao carrinho! ")
        total_da_compra += 15.60
    elif opcao == "4":
        print("Você adicionou Óleo ao carrinho! ")
        total_da_compra += 10.00
    elif opcao == "5":
        print("Você adicionou Açúcar ao carrinho! ")
        total_da_compra += 10.00
    opcao= input("lista de produtos: 1 - Arroz (R$ 25.00) , 2 - Feijão (R$ 19.50), 3 - Macarrão (R$ 15.60), 4 - Óleo (R$ 10.00), 5 - Açúcar (R$ 10.00), 6 - Finalizar compra. Digite o número do produto que deseja comprar: ")

print("== Quase finalizando sua compra! == ")

print("Sua Compra totalizou em R$: ", total_da_compra, " Obrigado por comprar conosco! ")



