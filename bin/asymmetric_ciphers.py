"""
MODULE NAME: asymmetric_ciphers
Author: Adisakshya Chauhan
"""

# import module helper_symmetric_ciphers 
from helper_asymmetric_ciphers import *

"""
Ron Rivest, Adi Shamir, Leonard (RSA) Cipher
"""
class rsa(object):

    # function to generate RSA keys
    def generate_rsa_keys(size):

        return RSA.generate(size)

    # function to encrypt message    
    def rsa_encrypt(rsa_public_key, message):

        obj = PKCS1_OAEP.new(rsa_public_key)
        return obj.encrypt(message.encode('utf-8'))

    # function to decrypt message
    def rsa_decrypt(rsa_key, cipher_text):

        obj2 = PKCS1_OAEP.new(rsa_key)
        return obj2.decrypt(cipher_text)

"""
Viginere Cipher
"""
class viginere_cipher(object):

    def encrypt(plaintext, key):
        
        pass


    def decrypt(ciphertext, key):
        
        pass

"""
Caesar Cipher
"""
class caesar_cipher(object):

    # function to encrypt message
    def encrypt(message,s): 
        
        cipher_text = "" 
  
        # traverse text 
        for i in range(len(message)): 
            
            char = message[i] 
  
            # Encrypt uppercase characters 
            if (char.isupper()): 
                
                cipher_text += chr((ord(char) + s-65) % 26 + 65) 
  
            # Encrypt lowercase characters 
            else: 
                
                cipher_text += chr((ord(char) + s - 97) % 26 + 97) 
  
        return cipher_text

    def decrypt(cipher_text, s):

        pass    

"""
PlayFair Cipher
"""

class playfair_cipher(object):   

    def chunker(seq, size):
        
        it = iter(seq)
        while True:
            
            chunk = tuple(itertools.islice(it, size))
            if not chunk:
            
                return
            
            yield chunk

    def prepare_input(dirty):
        
        """
        Prepare the plaintext by up-casing it
        and separating repeated letters with X's
        """
    
        dirty = ''.join([c.upper() for c in dirty if c in string.ascii_letters])
        clean = ""
    
        if len(dirty) < 2:
        
            return dirty

        for i in range(len(dirty)-1):
        
            clean += dirty[i]
        
            if dirty[i] == dirty[i+1]:
        
                clean += 'X'
    
        clean += dirty[-1]

        if len(clean) & 1:
        
            clean += 'X'

        return clean

    def generate_table(key):

        # I and J are used interchangeably to allow
        # us to use a 5x5 table (25 letters)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        # we're using a list instead of a '2d' array because it makes the math 
        # for setting up the table and doing the actual encoding/decoding simpler
        table = []

        # copy key chars into the table if they are in `alphabet` ignoring duplicates
        for char in key.upper():
        
            if char not in table and char in alphabet:
                table.append(char)

        # fill the rest of the table in with the remaining alphabet chars
        for char in alphabet:
        
            if char not in table:
                table.append(char)

        return table

    def encrypt(plaintext, key):
        
        table = generate_table(key)
        plaintext = prepare_input(plaintext)
        ciphertext = ""

        # https://en.wikipedia.org/wiki/Playfair_cipher#Description
        for char1, char2 in chunker(plaintext, 2):
        
            row1, col1 = divmod(table.index(char1), 5)
            row2, col2 = divmod(table.index(char2), 5)

            if row1 == row2:
        
                ciphertext += table[row1*5+(col1+1)%5]
                ciphertext += table[row2*5+(col2+1)%5]
        
            elif col1 == col2:
        
                ciphertext += table[((row1+1)%5)*5+col1]
                ciphertext += table[((row2+1)%5)*5+col2]
        
            else: # rectangle
        
                ciphertext += table[row1*5+col2]
                ciphertext += table[row2*5+col1]

        return ciphertext


    def decrypt(ciphertext, key):
        
        table = generate_table(key)
        plaintext = ""

        # https://en.wikipedia.org/wiki/Playfair_cipher#Description
        for char1, char2 in chunker(ciphertext, 2):
        
            row1, col1 = divmod(table.index(char1), 5)
            row2, col2 = divmod(table.index(char2), 5)

            if row1 == row2:
        
                plaintext += table[row1*5+(col1-1)%5]
                plaintext += table[row2*5+(col2-1)%5]
        
            elif col1 == col2:
        
                plaintext += table[((row1-1)%5)*5+col1]
                plaintext += table[((row2-1)%5)*5+col2]
        
            else: # rectangle
        
                plaintext += table[row1*5+col2]
                plaintext += table[row2*5+col1]

        return plaintext

"""
Polybius Square Cipher
"""
def polybius_square_cipher(oject):
    
    def encrypt(s):

        # convert each character to its encrypted code 
        for char in s: 
              
                # finding row of the table 
                row = int((ord(char) - ord('a')) / 5) + 1
          
                # finding column of the table  
                col = ((ord(char) - ord('a')) % 5) + 1
  
                # if character is 'k' 
                if char == 'k': 
        
                        row = row - 1
                        col = 5 - col + 1
                          
                # if character is greater than 'j' 
                elif ord(char) >= ord('j'): 
        
                        if col == 1 : 
                            col = 6
                            row = row - 1
                              
                        col = col - 1
                          
                print(row, col, end ='', sep ='')

    def decrypt(cipher_text):

        pass            

"""
Serpant Cipher
"""
class serpant(object):
    
    def encrypt(message):

        pass

    def decrypt(message):

        pass
