import random
import os

firstTime = True
score = 0


def check_folder():
    if os.path.exists("C:\\Users\\yourf\\AppData\\Roaming\\rock-paper-scissors"):
        pass
    else:
        os.mkdir("C:\\Users\\yourf\\AppData\\Roaming\\rock-paper-scissors")


def check_file():
    if os.path.exists("C:\\Users\\yourf\\AppData\\Roaming\\rock-paper-scissors\\data.txt"):
        fileExist = True
        pass
    else:
        f = open("C:\\Users\\yourf\\AppData\\Roaming\\rock-paper-scissors\\data.txt", "x")
        f.close()
        fileExist = False

    return fileExist


def player_throw():
    myThrow = str(input("Rock, Paper, Scissors? (r/p/s): "))
    print("")

    validInput = ['r', 'p', 's']

    while not myThrow.lower() in validInput:
        myThrow = str(input("Rock, Paper, Scissors? (r/p/s): "))
        print("")

    return myThrow


def bot_throw():
    botThrow = random.choice(['r', 'p', 's'])
    return botThrow


def process(myThrow, botThrow):
    global win
    if myThrow == botThrow:
        if myThrow == "r":
            outcome = "Rock"
        elif myThrow == "p":
            outcome = "Paper"
        else:
            outcome = "Scissors"
        print(f"It's a tie! You both played {outcome}.")
        win = False
    elif myThrow == "r" and botThrow == "p":
        print("Bot played Paper!")
        print("The bot won!")
        win = False
    elif myThrow == "r" and botThrow == "s":
        print("Bot played Scissors!")
        print("You won!")
        win = True
    elif myThrow == "p" and botThrow == "s":
        print("Bot played Scissors!")
        print("The bot won!")
        win = False
    elif myThrow == "p" and botThrow == "r":
        print("Bot played Rock!")
        print("You won!")
        win = True
    elif myThrow == "s" and botThrow == "p":
        print("Bot played Paper!")
        print("You won!")
        win = True
    elif myThrow == "s" and botThrow == "r":
        print("Bot played Rock!")
        print("The bot won!")
        win = False

    return win


def score_update(win):
    global score
    if win:
        score += 1


def main():
    check_folder()
    fileExists = check_file()

    if not fileExists:
        f = open("C:\\Users\\yourf\\AppData\\Roaming\\rock-paper-scissors\\data.txt", "w")
        name = str(input("Welcome to Rock Paper Scissors! To begin, enter your name: "))
        highscore = 0
        f.writelines([name, "\n", str(highscore)])
        f.close()

        myThrow = player_throw()
        botThrow = bot_throw()

        win = process(myThrow, botThrow)
        score_update(win)
        repeat(highscore, [name + "\n", "0"])
    else:
        f = open("C:\\Users\\yourf\\AppData\\Roaming\\rock-paper-scissors\\data.txt", "r")
        data = f.readlines()
        name = data[0].rstrip()
        highscore = data[1]

        global firstTime
        if firstTime:
            print(f"Welcome back, {name}! You know how this works. Highscore: {highscore}")

        myThrow = player_throw()
        botThrow = bot_throw()

        win = process(myThrow, botThrow)
        firstTime = False
        score_update(win)
        repeat(highscore, data)


def repeat(highscore, data):
    repeat = str(input("Do you want to play again? (y/n): "))

    validYesNo = ['y', 'n', 'Y', 'N']

    while not repeat in validYesNo:
        repeat = str(input("Do you want to play again? (y/n): "))

    if repeat.lower() == 'y':
        main()
    else:
        print("Thanks for playing!")
        global score
        if score > int(highscore):
            highscore = score
            data[1] = str(highscore)
            f = open("C:\\Users\\yourf\\AppData\\Roaming\\rock-paper-scissors\\data.txt", "w")
            f.writelines(data)
            f.close()


main()
