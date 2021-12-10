def caesar(start_text, shift_amount, word_direction):
    end_text = ""
    if word_direction == "decode":
        shift_amount *= -1
    for n in start_text:
        if n in alphabet:
            position = alphabet.index(n)
            new_position = position + shift_amount
            new_word = alphabet[new_position]
            end_text += new_word
        else:
            end_text += n

    print(f"The word is {end_text}")


from art import logo
print(logo)
state = True
while state:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, word_direction=direction)

    ask = input("Do you want run again?\n").lower()
    if ask == "yes":
        state = True
    else:
        print('Ok Goodbye')
        state = False



