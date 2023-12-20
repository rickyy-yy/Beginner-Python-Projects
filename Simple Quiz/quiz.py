def new_game():
    guesses = []
    correctGuesses = 0
    currentQuestionNumber = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[currentQuestionNumber - 1]:
            print(i)

        print("")
        guess = input("Enter your answer (A/B/C/D): ").upper()
        guesses.append(guess)

        correctGuesses += check_answer(questions.get(key), guess)

        currentQuestionNumber += 1

    display_score(correctGuesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(score):
    print(f"Your score is {score}!")


def play_again():
    play = input("Would you like to play again? (Y/N): ").upper()

    if play == "Y":
        new_game()
    else:
        print("Thank you for playing!")


questions = {"Who is the first president of the United States?": "A",
             "When was World War 1?": "C",
             "What shape is the moon?": "A",
             "What is 1kg in grams?": "B",
             "What is the second color of the rainbow?": "B"}

options = [["A) George Washington", "B) Abraham Lincoln", "C) Richard Nixon", "D) John F. Kennedy"],
           ["A) 1911", "B) 1927", "C) 1914", "D) 1899"],
           ["A) Circle", "B) Rectangle", "C) Donut", "D) Triangle"],
           ["A) 100", "B) 1000", "C) 2500", "D) 250"],
           ["A) Red", "B) Orange", "C) Blue", "D) Green"]]


new_game()
