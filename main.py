from morse_to_en import morse_to_english
from en_to_morse import english_to_morse


def option_check():
    return int(input("\nFor English to Morse code press '1',\n"
                     "For Morse code to English pres '2',\n"
                     "For existing the program press '3': "))


keep_going = True

while keep_going:
    result = option_check()
    if result == 1:
        english_to_morse()
    elif result == 2:
        morse_to_english()
    elif result == 3:
        keep_going = False
        break
    else:
        print("Invalid input. Please try again.")
