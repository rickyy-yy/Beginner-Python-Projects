def choose_mode():
    print("╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮")
    print("┃╭━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮")
    print("┃╰━━┳━╮╭━━┳━┳╮╱╭┳━┻╮╭╋━━╮╱╱┃┃┃┣━━┳━━┳━┳╮╱╭┳━┻╮╭╋━━╮")
    print("┃╭━━┫╭╮┫╭━┫╭┫┃╱┃┃╭╮┃┃┃╭╮┣━━┫┃┃┃┃━┫╭━┫╭┫┃╱┃┃╭╮┃┃┃╭╮┃")
    print("┃╰━━┫┃┃┃╰━┫┃┃╰━╯┃╰╯┃╰┫╰╯┣━┳╯╰╯┃┃━┫╰━┫┃┃╰━╯┃╰╯┃╰┫╰╯┃")
    print("╰━━━┻╯╰┻━━┻╯╰━╮╭┫╭━┻━┻━━╯╱╰━━━┻━━┻━━┻╯╰━╮╭┫╭━┻━┻━━╯")
    print("╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃┃┃")
    print("╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╰╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╰╯")

    print("")

    print("Select a mode:")
    print("A) Encrypter")
    print("B) Decrypter")
    print("")

    mode = input("Your choice: ").lower()

    while mode != "a" and mode != "b":
        print("You can only choose either A or B.")

        mode = input("Your choice: ").lower()

    if mode == "a":
        return 0
    else:
        return 1


def get_input(mode):
    if mode == 0:
        unprocessedString = str(input("Enter the string which you want to encrypt: "))
    else:
        unprocessedString = str(input("Enter the string which you want to decrypt: "))

    return unprocessedString


def encrypt_input(unprocessedString):
    processedString = ""
    encrypt_cipher = {"a": "c",
                      "b": "d",
                      "c": "e",
                      "d": "f",
                      "e": "g",
                      "f": "h",
                      "g": "i",
                      "h": "j",
                      "i": "k",
                      "j": "l",
                      "k": "m",
                      "l": "n",
                      "m": "o",
                      "n": "p",
                      "o": "q",
                      "p": "r",
                      "q": "s",
                      "r": "t",
                      "s": "u",
                      "t": "v",
                      "u": "w",
                      "v": "x",
                      "w": "y",
                      "x": "z",
                      "y": "a",
                      "z": "b"
                      }

    for i in range(1, len(unprocessedString) + 1):
        try:
            processedString = processedString + encrypt_cipher[unprocessedString[i - 1].lower()]
        except KeyError:
            processedString = processedString + unprocessedString[i - 1]

    return processedString


def decrypt_input(unprocessedString):
    processedString = ""
    decrypt_cipher = {"a": "y",
                      "b": "z",
                      "c": "a",
                      "d": "b",
                      "e": "c",
                      "f": "d",
                      "g": "e",
                      "h": "f",
                      "i": "g",
                      "j": "h",
                      "k": "i",
                      "l": "j",
                      "m": "k",
                      "n": "l",
                      "o": "m",
                      "p": "n",
                      "q": "o",
                      "r": "p",
                      "s": "q",
                      "t": "r",
                      "u": "s",
                      "v": "t",
                      "w": "u",
                      "x": "v",
                      "y": "w",
                      "z": "x"
                      }

    for i in range(1, len(unprocessedString) + 1):
        try:
            processedString = processedString + decrypt_cipher[unprocessedString[i - 1].lower()]
        except KeyError:
            processedString = processedString + unprocessedString[i - 1]

    return processedString


def start_again():
    play_again = str(input("Do you wish to use the encrypter/decrypter? (y/n) | ")).lower()

    while play_again != "y" and play_again != "n":
        print("You can only choose Y or N!")
        play_again = str(input("Do you wish to use the encrypter/decrypter? (y/n) | ")).lower()

    if play_again == "y":
        main()
    else:
        print("Thank you for using my code. Goodbye!")


def main():
    mode = choose_mode()

    unprocessedString = get_input(mode)

    if mode == 0:
        processedString = encrypt_input(unprocessedString)

        print(f"Your encrypted string is: {processedString}")
    else:
        processedString = decrypt_input(unprocessedString)

        print(f"Your decrypted string is: {processedString}")

    start_again()


main()
