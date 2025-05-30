from word_game import WordGame

def test_first_question_answer():
    game = WordGame("Tester", 10)
    assert game.questions[0]["answer"].lower() == "berlin"