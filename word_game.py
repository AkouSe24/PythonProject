
import json

class WordGame:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0
        self.questions = self.load_questions()

    def load_questions(self):
        try:
            with open("questions.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("❌ Error loading questions.")
            return []

    def start(self):
        print(f"\n👋 Welcome, {self.name}!")
        if self.age < 7:
            print("❌ You're too young for this game.")
            return
        elif self.age >= 13:
            print("⚠ This game may be too easy for you!")
        print("\n🎮 Let's begin the quiz!")
        self.run_quiz()
        self.save_score()

    def run_quiz(self):
        for i, q in enumerate(self.questions, 1):
            question = q.get("Questions")
            options = q.get("Options")
            answer = q.get("answer")

            print(f"\nQ{i}: {question}")
            for idx, opt in enumerate(options, 1):
                print(f"{idx}. {opt}")

            user_input = input("Choose your answer (option text or number): ").strip().lower()

            if user_input.isdigit():
                index = int(user_input) - 1
                if 0 <= index < len(options):
                    user_answer = options[index].lower()
                else:
                    print("⚠ Invalid number.")
                    continue
            else:
                user_answer = user_input

            if user_answer == answer.lower():
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong. The correct answer was: {answer}")

    def save_score(self):
        print(f"\n🏁 Game Over! Your final score is {self.score}.")


if __name__ == "__main__":
    name = input("Enter your name: ")
    age_input = input("Enter your age: ")

    try:
        age = int(age_input)
    except ValueError:
        print("⚠ Age must be a number.")
        exit()

    game = WordGame(name, age)
    game.start()