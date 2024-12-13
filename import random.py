import random
def get_random_word():
    words = ['эскалатор']
    return random.choice(words)
def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
        """,
        """
            --------
            |      |
            |      O
            |     /|\\
            |     
            |
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """,
        """
           --------
           |
           |
           |
           |
           |
        """
    ]
    return stages[tries]
def play_hangman():
    word = get_random_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Давайте сыграем в Виселицу!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Угадайте букву или слово: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже угадали эту букву:", guess)
            elif guess not in word:
                print("Этой буквы нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Хорошо! Это буква:", guess)
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Вы уже угадали это слово:", guess)
            elif guess != word:
                print("Это не то слово.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Поздравляем! Вы угадали слово:", word)
    else:
        print("Вы проиграли. Загаданное слово было:", word)
if __name__ == "__main__":
    play_hangman()

