nota_1 = float(input("Digite a Primeira Nota: "))
nota_2 = float(input("Digite a segunda Nota: "))
nota_3 = float(input("Digite a terceira Nota: "))

soma = nota_1 + nota_2 + nota_3
media = soma / 3

if media >= 6:
    print("Aluno Aprovado!!")
elif media >= 4 and media < 6:
    print("Aluno em Recuperação!!")
else: 
    print("Aluno Reprovado!!")



                     