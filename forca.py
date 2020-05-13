import random


def play():
    display_welcome_message()
    secret_word = choose_secret_word()
    correct_letters = init_correct_letters(secret_word)

    errors = 0
    hanged = False
    win = False

    print(correct_letters)

    while not hanged and not win:
        guess = request_guess()

        if guess in secret_word:
            mark_guess_as_correct(correct_letters, guess, secret_word)
        else:
            errors += 1
            draw_hang(errors)

        hanged = errors == 7
        win = "_" not in correct_letters

        print(correct_letters)

    if win:
        display_winner_message()
    else:
        display_loser_message(secret_word)


def display_loser_message(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def display_winner_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mark_guess_as_correct(accepted_letters, guess, secret_word):
    index = 0
    for letter in secret_word:
        if guess == letter:
            accepted_letters[index] = letter

        index += 1


def display_welcome_message():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")


def choose_secret_word():
    words = []

    with open("words.txt", "r") as file:
        for line in file:
            words.append(line.strip())

    word_index = random.randrange(0, len(words))
    secret_word = words[word_index]
    secret_word = secret_word.upper()

    return secret_word


def request_guess():
    guess = input("\nQual letra? ")
    guess = guess.strip().upper()
    return guess


def init_correct_letters(word):
    return ["_" for letter in word]


def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
