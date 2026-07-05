print("==== TABUADA ==== ")

numero = int(input("Digite um número para ver a tabuada: "))
print("Aqui está a tabuada do número", numero)
for i in range (10,0,-1):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)