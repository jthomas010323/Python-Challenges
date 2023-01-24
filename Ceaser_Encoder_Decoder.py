def encrypt(text, shift):
    for i in range(len(text)):
        word_list=list(text)
        letter_index=alphabet.index(text[i])
        letter_index=letter_index+shift
        word_list[i]=alphabet[letter_index]
        text=''.join(word_list)
    print(text)

def decrypt(text, shift):
    for i in range(len(text)):
        word_list=list(text)
        letter_index=alphabet.index(text[i])
        letter_index=abs(letter_index-shift)
        word_list[i]=alphabet[letter_index]
        text=''.join(word_list)
    print(text)

def ceaser(text, shift, direction):
    if direction=="encode":
        encrypt(text, shift)
    elif direction=="decrypt":
        decrypt(text, shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

ceaser(text, shift, direction)