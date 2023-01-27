from alphabet import morse_alphabet


def morse_to_english():
    morse_sentence = input("Write your morse code here (separate letters with spaces and words with '/': ")
    new_english = ""
    if "/" in morse_sentence:
        new_english = morse_sentence.replace("/", " / ")
    else:
        new_english = morse_sentence

    letters_without_spaces = new_english.split()

    def get_key(letter):
        english_result = ""
        for key, value in morse_alphabet.items():
            if letter == value:
                english_result += key
        print(english_result, end="")

    for letter in letters_without_spaces:
        get_key(letter)
