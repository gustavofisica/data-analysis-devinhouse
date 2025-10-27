import random

def main():
    valor = random.randint(1, 100)
    print(valor)
    while True:
        chute = int(input("Faça seu chute de 0 a 100: "))
        if chute > valor:
            dica = random.randint(0, 2)
            match dica:
                case 0:
                    print("Seu chute foi maior que o número secreto. Tente um valor menor!")
                case 1:
                    print("Quase lá! O número é menor do que seu palpite.")
                case 2:
                    print("Passou do número! Diminua seu chute.")
        elif chute < valor:
            dica = random.randint(0, 2)
            match dica:
                case 0:
                    print("Seu chute foi menor que o número secreto. Tente um valor maior!")
                case 1:
                    print("Quase lá! O número é maior do que seu palpite.")
                case 2:
                    print("Faltou pouco! Aumente seu chute.")
        elif chute == valor:
            print("Parabéns! Você acertou o número secreto!")
            print("Obrigado por jogar! Tente novamente para se desafiar.")
            break


if __name__ == "__main__":
    main()
