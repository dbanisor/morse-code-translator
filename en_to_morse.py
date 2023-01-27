from alphabet import morse_alphabet


def english_to_morse():
    sentence = input("Write your message in English here: ")

    for char in sentence:
        if char == " ":
            print(" ", end="     ")
        else:
            print(morse_alphabet[char], end="")
