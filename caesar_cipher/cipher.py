# ord() turns a letter into a unicode number
# chr() turns a unicode number into a letter
# % or modulus helps you wrap around the alphabet after shifting 26 characters. 
# An a shifted 26 times is also an a

from .corpus_loader import word_list, name_list


def encrypt(string, shift):
    """This should be encrypting a string based on the string and a shift. Issues abound with counting out and wrapping the characters."""
    shifted = ""
    for letter in string:
        number = ord(letter) 
        number += shift %26
        # Add the shift value - remainder only
        new = chr(number)
        shifted += new
        print(number)
    return shifted

def decrypt(encrpyted_text, shift):
    """Returns the opposite shift to slide the message back to the pre-encrypted version"""
    return encrypt(encrpyted_text, -shift)

def crack(secret_message):
    """Check the 25 shifts of a message. If more than 80% of the returned words are words, return the decrypted message. Else, nothing will be returned. Having some issue with the nltk pip install."""
    for i in range(0,25):
        shh = encrypt(secret_message, i)
        yes = 0
        no = 0
        for word in shh.split():
            # Break up the sentence into individual words
            if word in word_list or name_list:
                yes += 1
            else:
                no +=1
        if yes/(yes+no) >.8:
            return shh
        else:
            continue
    
            


