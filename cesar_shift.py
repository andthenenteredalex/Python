""" Copyright Alex Clark
    
    Written in Python 2.7.13
    November 2017
    
    This is a cesar shift, in every combination I have tested it works perfectly, shifting the numbers around the alphabet, z + 2 equaling b for example and e - 7 equaling y.
    
    I'm going to make it more efficient and eliminate the '','', etc. in the arrays. Future developments are to include ways to paste in entire messages and maybe save results as a separate file, or import a file to be encrypted. The possibilities are endless! But let me know if you have any questions, I'll be updating this as soon as I can.
    
    Cheers,
    -Alex
    
    """


def decrypt_cesar(new_word, number): #3
    """ decrypts the cesar shift encryption and prints a string """
    decrypted_num = []
    for char in new_word:
        char = ord(char)
        decrypted_num.append(char)

    decrypted_word = []
    for num in decrypted_num:
        if (num - number) < 97:
            a = 97 - num
            num = 97 - a # 117 - a = 121
            num = chr(num)
            decrypted_word.append(num)
        else:
            num = chr(num)
            decrypted_word.append(num)
    print decrypted_word
    print "\n"

def encrypt_cesar(word, number): # 1
    """ takes a word and a number to shift by as input and prints the encrypted contents of an array. """
    cesar = []
    for char in word:
        new_num = (ord(char) + number)
        if new_num > 122:
            a = new_num - 122
            character = a + 97
            cesar.append(character)
        else:
            cesar.append(new_num)
    new_word = []
    for char in cesar:
        char = int(char)
        new_word.append(chr(char))
    print "\n"
    print new_word

word = raw_input("Enter a word for me to encrypt: ")
number = int(raw_input("Enter a number between 1 and 26 by which to shift: "))

encrypt_cesar(word, number)

new_word = word
time = raw_input("""
    
    
    Press enter to decrypt
    
    
    """)
decrypt_cesar(new_word, number)
