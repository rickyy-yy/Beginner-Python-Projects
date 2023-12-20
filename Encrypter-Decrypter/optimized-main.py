def choose_mode():
    print("Select a mode:")
    print("A) Encrypter")
    print("B) Decrypter")
    print("")

    mode = input("Your choice: ").lower()

    while mode != "a" and mode != "b":
        print("You can only choose either A or B.")

        mode = input("Your choice: ").lower()

    return mode


def get_input(mode):
    if mode == "a":
        prompt = "Enter the string which you want to encrypt: "
    else:
        prompt = "Enter the string which you want to decrypt: "

    return input(prompt)


def shift_letter(letter, shift):
    """
    Shifts a letter by the specified amount.
    If the letter is uppercase, the resulting letter will also be uppercase.
    If the letter is not an alphabet letter, it will not be changed.
    """
    is_upper = letter.isupper()
    letter = letter.lower()

    # Calculate the index of the letter in the alphabet
    index = ord(letter) - ord('a')

    # Shift the index and keep it within the range of alphabet indices
    index = (index + shift) % 26

    # Convert the index back to a letter
    result = chr(index + ord('a'))

    # Preserve the case of the original letter
    if is_upper:
        result = result.upper()

    return result


def process_input(unprocessedString, shift):
    processedString = ""

    for letter in unprocessedString:
        if letter.isalpha():
            processedString += shift_letter(letter, shift)
        else:
            processedString += letter

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

    if mode == "a":
        processedString = process_input(unprocessedString, 1) # Encrypt by shifting one position to the right
        action = "encrypted"
    else:
        processedString = process_input(unprocessedString, -1) # Decrypt by shifting one position to the left
        action = "decrypted"

    print(f"Your {action} string is: {processedString}")

    start_again()


main()
