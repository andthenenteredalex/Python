plaintext = open('plain.txt')
ciphertext = open('cipher.txt', 'w')
word = plaintext.read()

def encrypt_cesar(word, number): # 1
    """ takes a word and a number to shift by as input and prints the encrypted contents of an array. """
    cesar = []
    for char in word:
        new_num = (ord(char) + number)
        cesar.append(new_num)

    new_word = []
    for char in cesar:
        char = int(char)
        new_word.append(chr(char))

    return "".join(new_word)



number = int(raw_input("Enter a number between 1 and 26 by which to shift: "))
ciphertext.write(encrypt_cesar(word, number))
ciphertext.close()

