from word_game import WordGame

if __name__ == "_main_":
    print("🧠 Welcome to WordQuiz Game!")
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("❌ Please enter a valid number for age.")
        exit()

    game = WordGame(name, age)
    game.start()
