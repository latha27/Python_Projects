
MORSE_CODE = {"A": "*-", "B": "-***", "C": "-*-*", "D": "-**", "E": "*", "F": "**-*", "G": "--*", "H": "****",
              "I": "**", "J": "*---", "K": "-*-", "L": "*-**", "M": "--", "N": "-*", "O": "---", "P": "*--*",
              "Q": "--*-", "R": "*-*", "S": "***", "T": "-", "U": "**-", "V": "***-", "W": "*--", "X": "-**-",
              "Y": "-*--", "Z": "--**"
}
'''
user_input = input("Enter the text to convert to morse code:").upper()

converted_string = ''

for letter in user_input:
    converted_letter = MORSE_CODE[letter]
    converted_string = converted_string + converted_letter
print(converted_string) '''


def encode(text):
    encode_word = []
    for letter in text.upper():
        encode_word.append(MORSE_CODE[letter])
    print(encode_word)



def decode_morse(morse_code):
    word = []
    for code in morse_code:
        for key, value in MORSE_CODE.items():
            if code == value:
                word.append(key)
    print(word)

encode(text="Python")
decode_morse(['*--*', '-*--', '-', '****', '---', '-*'])


