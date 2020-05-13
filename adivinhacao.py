import random


def play():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    tries = 0
    points = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    level = int(input("Defina o nível: "))

    if level == 1:
        tries = 20
    elif level == 2:
        tries = 10
    else:
        tries = 5

    for round in range(1, tries + 1):
        print("Tentativa {} de {}".format(round, tries))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        guess = int(chute_str)

        if guess < 1 or guess > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        hit = guess == secret_number
        greater = guess > secret_number
        lesser = guess < secret_number

        if hit:
            print("Você acertou e fez {} pontos!".format(points))
            break
        else:
            if greater:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif lesser:
                print("Você errou! O seu chute foi menor do que o número secreto.")

            lost_points = abs(secret_number - guess)
            points = points - lost_points

    print("Fim do jogo")


if __name__ == "__main__":
    play()
