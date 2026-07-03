numero1 = int(input("Digite um Número: "))
numero2 = int(input("Digite outro Número: "))

print("Escolha uma operação: ")
opcao = int(input("Escolha 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão: "))

if numero1 == 0 or numero2 == 0:
    print("Não é possível realizar operações com zero.")
elif opcao == 1:
    resultado = numero1 + numero2
    print(f"O resultado da sua operação é: {resultado}")
elif opcao == 2:
    resultado = numero1 - numero2
    print(f"O resultado da sua operação é: {resultado}")
elif opcao == 3:
    resultado = numero1 * numero2
    print(f"O resultado da sua operação é: {resultado}")
elif opcao == 4:
    resultado = numero1 / numero2
    print(f"O resultado da sua operação é: {resultado}")
else: 
    print("Opção inválida. Por favor, escolha uma operação válida.")