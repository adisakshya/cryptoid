"""
MODULE NAME: symmetric_ciphers
Author: Adisakshya Chauhan
version: 1.2
"""

# import module helper 
from helper import *

# BLOCK CIPHERS
"""
Advance Encryption Standard (AES)
MODES:
    1. ECB
    2. CBC
    3. CFB
    4. OFB
    5. CTR
    6. EAX
BLOCK_SIZE: 16
KEY_SIZE = (16, 24, 32)
"""
class aes(object):

    # functtion to generate key of length - (size) bytes
    def generate_key(size):

        # return generated key as byte object
        return AES.get_random_bytes(size)

    # function to return ciphertext
    def encrypt(message, key, mode_no=1, iv='This is an IV456'):

        try:
            
            # create new AES cipher
            obj = create_instance(1, key, mode_no, iv)
            
            # padding
            message = padding(message,16)

            # get cipher_text
            cipher_text = get_cipher_text(obj, message)
            #cipher_text = str(cipher_text, 'utf-8')

            # return cipher_text
            return cipher_text                         
        
        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

    # function to decrypt ciphertext
    def decrypt(cipher_text, key, mode_no=1, iv='This is an IV456'):
        
        try:
            
            # create new AES cipher
            obj = create_instance(1, key, mode_no, iv)
            
            # return original message
            message =  get_original_message(obj,cipher_text)

            # remove padding
            message = str(message, 'utf-8')
            message = message.strip(' ')

            # return original message
            return message

        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))


"""
Data Encryption Standard (DES)
MODES:
    1. ECB
    2. CBC
    3. CFB
    4. OFB
    5. CTR
    6. EAX
BLOCK_SIZE: 8
KEY_SIZE = 8
"""
class des(object):

    # function to return ciphertext
    def encrypt(message, key, mode_no=1, iv='This is an IV456'):

        try:
            
            # create new DES cipher
            obj = create_instance(2, key, mode_no, iv)
            
            # padding
            message = padding(message,8)

            # get cipher_text
            cipher_text = get_cipher_text(obj, message)
            #cipher_text = str(cipher_text, 'utf-8')

            # return cipher_text
            return cipher_text                         
        
        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

    # function to decrypt ciphertext
    def decrypt(cipher_text, key, mode_no=1, iv='This is an IV456'):
        
        try:
            
            # create new DES cipher
            obj = create_instance(2, key, mode_no, iv)
            
            # return original message
            message =  get_original_message(obj,cipher_text)

            # remove padding
            message = str(message, 'utf-8')
            message = message.strip(' ')

            # return original message
            return message

        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))


"""
Triple Data Encryption Standard (DES3)
MODES:
    1. ECB
    2. CBC
    3. CFB
    4. OFB
    5. CTR
    6. EAX
BLOCK_SIZE: 8
KEY_SIZE = (16, 24) ------ 8*3 == 24 -----------
"""
class triple_des(object):

    # function to return ciphertext
    def encrypt(message, key, mode_no=1, iv='This is an IV456'):

        try:
            
            # create new DES3 cipher
            obj = create_instance(2, key, mode_no, iv)
            
            # padding
            message = padding(message,8)

            # get cipher_text
            cipher_text = get_cipher_text(obj, message)
            #cipher_text = str(cipher_text, 'utf-8')

            # return cipher_text
            return cipher_text                         
        
        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

    # function to decrypt ciphertext
    def decrypt(cipher_text, key, mode_no=1, iv='This is an IV456'):
        
        try:
            
            # create new DES3 cipher
            obj = create_instance(2, key, mode_no, iv)
            
            # return original message
            message =  get_original_message(obj,cipher_text)

            # remove padding
            message = str(message, 'utf-8')
            message = message.strip(' ')

            # return original message
            return message

        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))


"""
Rivest's Cipher version 2 (RC2)
MODES:
    1. ECB
    2. CBC
    3. CFB
    4. OFB
    5. CTR
    6. EAX
BLOCK_SIZE: 8
KEY_SIZE: (5, 129)    
"""
class rc2(object):

    # function to return ciphertext
    def encrypt(message, key, mode_no=1, iv='This is an IV456'):

        try:
            
            # create new RC2 cipher
            obj = create_instance(4, key, mode_no, iv)
            
            # padding
            message = padding(message,16)

            # get cipher_text
            cipher_text = get_cipher_text(obj, message)
            #cipher_text = str(cipher_text, 'utf-8')

            # return cipher_text
            return cipher_text                         
        
        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

    # function to decrypt ciphertext
    def decrypt(cipher_text, key, mode_no=1, iv='This is an IV456'):
        
        try:
            
            # create new RC2 cipher
            obj = create_instance(4, key, mode_no, iv)
            
            # return original message
            message =  get_original_message(obj,cipher_text)

            # remove padding
            message = str(message, 'utf-8')
            message = message.strip(' ')

            # return original message
            return message

        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

"""
CAST
MODES:
    1. ECB
    2. CBC
    3. CFB
    4. OFB
    5. CTR
    6. EAX
BLOCK_SIZE: 8
KEY_SIZE = (5, 17)
"""
class cast(object):

    # function to return ciphertext
    def encrypt(message, key, mode_no=1, iv='This is an IV456'):

        try:
            
            # create new CAST cipher
            obj = create_instance(5, key, mode_no, iv)
            
            # padding
            message = padding(message,8)

            # get cipher_text
            cipher_text = get_cipher_text(obj, message)
            #cipher_text = str(cipher_text, 'utf-8')

            # return cipher_text
            return cipher_text                         
        
        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

    # function to decrypt ciphertext
    def decrypt(cipher_text, key, mode_no=1, iv='This is an IV456'):
        
        try:
            
            # create new CAST cipher
            obj = create_instance(5, key, mode_no, iv)
            
            # return original message
            message =  get_original_message(obj,cipher_text)

            # remove padding
            message = str(message, 'utf-8')
            message = message.strip(' ')

            # return original message
            return message

        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))


"""
Blowfish
MODES:
    1. ECB
    2. CBC
    3. CFB
    4. OFB
    5. CTR
    6. EAX
BLOCK_SIZE: 8
KEY_SIZE = (5, 57)
"""
class blowfish(object):

    # function to return ciphertext
    def encrypt(message, key, mode_no=1, iv='This is an IV456'):

        try:
            
            # create new Blowfish cipher
            obj = create_instance(6, key, mode_no, iv)
            
            # padding
            message = padding(message,8)

            # get cipher_text
            cipher_text = get_cipher_text(obj, message)
            #cipher_text = str(cipher_text, 'utf-8')

            # return cipher_text
            return cipher_text                         
        
        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

    # function to decrypt ciphertext
    def decrypt(cipher_text, key, mode_no=1, iv='This is an IV456'):
        
        try:
            
            # create new Blowfish cipher
            obj = create_instance(6, key, mode_no, iv)
            
            # return original message
            message =  get_original_message(obj,cipher_text)

            # remove padding
            message = str(message, 'utf-8')
            message = message.strip(' ')

            # return original message
            return message

        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))


# STREAM CIPHERS
"""
ARC4
BLOCK_SIZE: 1
KEY_SIZE = (16, 32)
"""
class rc4(object):

    # function to return ciphertext
    def encrypt(message, key):

        try:
            
            # create new ARC4 cipher
            obj = create_instance_2(7, key)
            
            # padding
            message = padding(message,1)

            # get cipher_text
            cipher_text = get_cipher_text(obj, message)
            #cipher_text = str(cipher_text, 'utf-8')

            # return cipher_text
            return cipher_text                         
        
        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

    # function to decrypt ciphertext
    def decrypt(cipher_text, key):
        
        try:
            
            # create new ARC4 cipher
            obj = create_instance_2(7, key)
            
            # return original message
            message =  get_original_message(obj,cipher_text)

            # remove padding
            message = str(message, 'utf-8')
            message = message.strip(' ')

            # return original message
            return message

        except Exception as error:
            
            # report error
            print('Caught this error: ' + repr(error))

"""
Salsa20
BLOCK_SIZE = 1
KEY_SIZE = 32
"""
class salsa20(object):

    def generate_key(size):

        return Salsa20.get_random_bytes(size)

    # function to return ciphertext
    def encrypt(message, secret):
        
        cipher = Salsa20.new(key = secret)
        msg = cipher.nonce + cipher.encrypt(message.encode('utf-8'))
        return msg

    # function to decrypt ciphertext
    def decrypt(msg, secret):        
        
        try:

            msg_nonce = msg[:8]
            cipher_text = msg[8:]
            cipher = Salsa20.new(key=secret, nonce=msg_nonce)            

        except Exception:

            msg_nonce = msg[:16]
            cipher_text = msg[16:]
            cipher = Salsa20.new(key=secret, nonce=msg_nonce)
        
        message = cipher.decrypt(cipher_text)
        return message        

"""
ChaCha20
BLOCK_SIZE = 1
KEY_SIZE = 32
"""
class chacha20(object):

    def generate_key(size):

        return ChaCha20.get_random_bytes(size)

    # function to return ciphertext
    def encrypt(message, secret):
        
        cipher = ChaCha20.new(key = secret)
        msg = cipher.nonce + cipher.encrypt(message.encode('utf-8'))
        return msg

    # function to decrypt ciphertext
    def decrypt(msg, secret):        
        
        msg_nonce = msg[:8]
        cipher_text = msg[8:]
        cipher = ChaCha20.new(key=secret, nonce=msg_nonce)
        message = cipher.decrypt(cipher_text)
        return message
