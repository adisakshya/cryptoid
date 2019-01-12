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
    def encrypt(rsa_public_key, message):

        obj = PKCS1_OAEP.new(rsa_public_key)
        return obj.encrypt(message.encode('utf-8'))

    # function to decrypt message
    def decrypt(rsa_key, cipher_text):

        obj2 = PKCS1_OAEP.new(rsa_key)
        return obj2.decrypt(cipher_text)

"""
Viginere Cipher
"""
class viginere_cipher(object):

    def encrypt(clear, key):
        
        enc = [] 
      
        for i in range(len(clear)): 
            key_c = key[i % len(key)] 
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256) 
                       
            enc.append(enc_c) 
          
        return "".join(enc) 
  


    def decrypt(enc, key):
        
        dec = [] 
      
        enc = base64.urlsafe_b64decode(enc).decode() 
        for i in range(len(enc)): 
            key_c = key[i % len(key)] 
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256) 
                             
            dec.append(dec_c) 
        return "".join(dec)

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
    
    def encrypt():

        pass

    def decrypt():

        pass

"""
Polybius Square Cipher
"""
class polybius_square_cipher(object):
    
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
