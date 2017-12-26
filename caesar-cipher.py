# caesar-cipher.py - a command line tool to decrypt messages using a Caesar Cipher
# Created by: mini-gui
# Date: December 2017


# imports
import sys
import argparse
import os
from time import sleep

# functions
def shift(index, key):
    """returns the modified index in recursive base 25"""
    if key >= 0:
        for i in range(key):
            index += 1
            if index > (len(crypt_base) - 1):
                index = 0
    else:
        for i in range(abs(key)):
            index -= 1
            if index < 0:
                index = (len(crypt_base) - 1)

    return index


def crypt(message):
    """given a message returns its encrypted version"""
    crypted_msg = ''
    global crypt_key

    for word in message.split(' '):
        crypted_word = ''
        for letter in word:
            crypted_word += crypt_base[shift(crypt_base.index(letter), crypt_key)]
        crypted_msg += crypted_word + ' '
    crypted_msg = crypted_msg[:-1]

    return crypted_msg


def crypt_file(path):
    """Encrypt the selected file"""
    with open(path, 'w') as f:
        lines = f.readlines()
        for line in lines:
            line = crypt(line)
            f.write(line)


# Parser settings
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help="Encrypt from txt file in specified path", action="store_true", dest="file_path")
parser.add_argument('-k', '--key', help="Change the encryption key", action="store", dest="key_stored")

# reference
crypt_base = 'abcdefghijklmnopqrstuvwxyz'


# main
if __name__ == '__main__':
# if no additional arguments is added to the script use interaction
    if len(sys.argv) == 1:
       crypt_key = int(input('What is the key?\n')) 

       msg = input('Input the message you need to crypt..\n').lower()
       print(2*'\n')
       sleep(0.2)

       print(crypt(msg))
        
    else:
# using argparse to handle positional argumets
        arguments = parser.parse_args()
# if the '-p' flag is true promtp to a file location
        if arguments.file_path:
            path_to_file = input('Select the file you want to encrypt\n')
            crypt_file(path_to_file)

# else use the '-k' flag to encrypt a message
        crypt_key = int(arguments.key_stored)
        msg = input('Input the message you need to encrypt..\n').lower()
        print(2*'\n')
        sleep(0.2)
        print(crypt(msg))
