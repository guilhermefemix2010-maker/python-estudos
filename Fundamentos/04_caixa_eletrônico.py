saldo = int (5000)
print("Seja bem vindo ao caixa eletrônico! ")
opção = int(input("Digite 1 para consultar o saldo, 2 para sacar, 3 para depositar e 4 para sair: "))

while opção != 4:
    if(opção == 1):
        print("seu saldo é de: RS ", saldo)
    elif(opção == 2):
        saque = int(input("Digite o valor que deseja sacar: "))
        if(saque > saldo):
            print ("Saldo insuficiente! ")
        else:
            saldo = saldo - saque
            print("Saque realizado com sucesso!, seu saldo é de RS ", saldo)
    elif(opção == 3 ):
        deposito = int(input("Digite o valor que deseja depositar: "))
        saldo = saldo + deposito
        print("Depósito realizado com sucesso!, seu saldo é de RS ", saldo)
    print("Seja bem vindo ao caixa eletrônico! ")
    opção = int(input("Digite 1 para consultar o saldo, 2 para sacar, 3 para depositar e 4 para sair: "))
   
print("Obrigado por utilizar o caixa eletrônico! ")
