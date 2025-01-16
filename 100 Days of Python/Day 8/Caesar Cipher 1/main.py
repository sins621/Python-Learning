alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# direction = input(
#     "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
# ).lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
direction = "encode"
text = "zolla"
shift = 1


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


def encrypt(original_text, shift_amount):
    cipher_text = ""  # change to list
    alphabet_length = len(alphabet)  # length of the alphabet list

    for l in original_text:
        shifted_index = alphabet.index(l) + shift_amount
        shifted_index %= alphabet_length

        cipher_text += alphabet[shifted_index]

    print(cipher_text)

def decrypt(original_text, shift_amount):
    cipher_text = ""  # change to list
    alphabet_length = len(alphabet)  # length of the alphabet list

    for l in original_text:
        shifted_index = alphabet.index(l) + shift_amount
        shifted_index %= alphabet_length

        cipher_text += alphabet[shifted_index * -1]

    print(cipher_text)

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
# encrypt("z", 9)
decrypt("hello", 3)

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
# encrypt(text, shift)
