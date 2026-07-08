print("==== Bem-vindo ao jogo da adivinhação! ====")

import random
numero_secreto = random.randint(1, 100)
tentativas= 0 
palpite=int(input("Digite um número entre 1 e 100: "))

while palpite != numero_secreto:
    tentativas += 1
    if palpite < numero_secreto:
        print("O número secreto é maior que o seu palpite. Tente novamente.")
        palpite=int(input("Digite um número entre 1 e 100: "))
    elif palpite > numero_secreto:
        print("O número secreto é menor que o seu palpite. Tente novamente.")
        palpite=int(input("Digite um número entre 1 e 100: "))
else: 
  palpite = numero_secreto
  print("Parabéns! Você acertou o número secreto em", tentativas, "tentativas.")