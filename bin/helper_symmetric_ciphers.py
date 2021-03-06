"""
MODULE NAME: helper_symmetric_ciphers
Author: Adisakshya Chauhan
"""

# import block ciphers from Crypto module
# to use thier functions to encrypt and decrypt
# messages
from Crypto.Cipher import AES, DES, DES3, ARC2, CAST, Blowfish

# import stream ciphers from Crypto module
# to use thier functions to encrypt and decrypt
# messages
from Crypto.Cipher import ARC4, Salsa20, ChaCha20

# list of all supported ciphers
ciphers_block = ['', AES, DES, DES3, ARC2, CAST, Blowfish, ARC4]
ciphers_stream = ['', ARC4, Salsa20, ChaCha20]

# list of all supported modes of operation
#modes = ['',MODE_ECB,MODE_CBC,MODE_CFB,MODE_OFB,MODE_CTR,MODE_EAX]
modes = ['', 1, 2, 3, 5, 6, 9]

# function to create a new block cipher and return it's instance
def create_instance(x, key, mode_no, iv):
    
    try:    
        
        # cases for auto-generated byte key or user input string key
        # for modes other than ECB and CTR
        try:
            
            return ciphers_block[x].new(key.encode('utf-8'), modes[mode_no], iv.encode('utf-8'))
        
        except Exception:
            
            return ciphers_block[x].new(key, modes[mode_no], iv.encode('utf-8'))

    except Exception:
        
        # cases for auto-generated byte key or user input string key
        # for modes ECB and CTR
        try:

            return ciphers_block[x].new(key.encode('utf-8'), modes[mode_no])
        
        except Exception:
            
            return ciphers_block[x].new(key, modes[mode_no])

# function to create a new stream cipher and return it's instance
def create_instance_2(x, key, msg_nonce):
    
    # cases for auto-generated byte key or user input string key
    try:
            
        try:
            return ciphers_stream[x].new(key=key.encode('utf-8'),nonce=msg_nonce)
        except:
            return ciphers_stream[x].new(key=key,nonce=msg_nonce)
        
    except Exception as error:

        print('Caught this error in creating instance: ' + repr(error))

# function to return cipher_text
def get_cipher_text(obj, message):

    try:

        return obj.encrypt(message.encode('utf-8'))

    except Exception as error:

        print('Caught this error in making cipher_text: ' + repr(error))

# function to return original message
def get_original_message(obj, cipher_text):

    try:

        return obj.decrypt(cipher_text)

    except Exception as error:

        print('Caught this error in getting original message back: ' + repr(error))    

# function to do padding of -----space----- on message
def padding(message, block_size):
    
    if len(message)%block_size == 0:
        return message
    else:
        padding_factor = (len(message)//block_size + 1)*block_size - len(message)  

    return (message + " "*padding_factor)
