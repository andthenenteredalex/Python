""" Copyright Alex Clark November 2017 """
ciphertext = open('cipher.txt')
plaintext = open('plain.txt', 'w')
new_word = ciphertext.read()

def decrypt_cesar(new_word, number): #3
    """ decrypts the cesar shift encryption and prints a string """
    decrypted_num = []
    for char in new_word:
        char = ord(char)
        decrypted_num.append(char)

    decrypted_word = []
    for num in decrypted_num:
        num = num - number
        decrypted_word.append(chr(num))

    return "".join(decrypted_word)


number = int(raw_input("Enter the number the text was shifted: "))

plaintext.write(decrypt_cesar(new_word, number))
plaintext.close()
