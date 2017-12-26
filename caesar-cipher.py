# caesar-cipher.py - a command line tool to decrypt messages using a Caesar Cipher
# Created by: mini-gui
# Date: December 2017


# imports
import sys
from time import sleep

# functions
def shift(index, key):
    """returns the modified index in recursive base 26"""
    if key >= 0:
        for i in range(key):
            index += 1
            if index > 25:
                index = 0
    if key < 0:
        for i in range(abs(key)):
            index -= 1
            if index < 0:
                index = 25

    return index

def crypt(message):
    """given a message returns its crypted version"""
    crypted_msg = ''
    global crypt_key

    for word in message.split(' '):
        crypted_word = ''
        for letter in word:
            crypted_word += alphabet[shift(alphabet.index(letter), crypt_key)]
        crypted_msg += crypted_word + ' '
    crypted_msg = crypted_msg[:-1]

    return crypted_msg


# index reference
alphabet = 'abcdefghijklmnopqrstuvwxyz'


# main
if __name__ == '__main__':
# no additional arguments added to the script
    if len(sys.argv) == 1:
       crypt_key = int(input('What is the key?\n')) 

       msg = input('Input the message you need to crypt..\n').lower()
       print(2*'\n')
       sleep(0.2)

       print(crypt(msg))
        
    else:
# using the '-k' flag to change the key-shift
        if sys.argv[1] == '-k':
            crypt_key = int(sys.argv[2])
            msg = input('Input the message you need to crypt..\n').lower()
            print(2*'\n')
            sleep(0.2)
            print(crypt(msg))

# unknown flag
        elif sys.argv[1][0] == '-' and sys.argv[1][1] != 'k':
            print('Sorry, unknown command')
            sys.exit()

# no flag uses the default caesar cypher
        else:
            crypt_key = -3
            msg = ' '.join(sys.argv[1:])
            print(2*'\n')
            sleep(0.2)
            print(crypt(msg))
