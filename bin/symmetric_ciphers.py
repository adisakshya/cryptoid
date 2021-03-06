"""
MODULE NAME: symmetric_ciphers
Author: Adisakshya Chauhan
"""

# import module helper_symmetric_ciphers 
from helper_symmetric_ciphers import *

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

    # function to return valid key size
    def get_valid_key_size():

        return [16, 24, 32]
    
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

    # function to return valid key size
    def get_valid_key_size():

        return [8]

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

    # function to return valid key size
    def get_valid_key_size():

        return [24]

    # function to return ciphertext
    def encrypt(message, key, mode_no=1, iv='This is an IV456'):

        try:
            
            # create new DES3 cipher
            obj = create_instance(3, key, mode_no, iv)
            
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
            obj = create_instance(3, key, mode_no, iv)
            
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

    # function to return valid key size
    def get_valid_key_size():

        return [x for x in range(5,130)]

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

    # function to return valid key size
    def get_valid_key_size():

        return [x for x in range(5,18)]

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

    # function to return valid key size
    def get_valid_key_size():

        return [x for x in range(5,58)]

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

    # function to return valid key size
    def get_valid_key_size():

        return [x for x in range(16,32)]

    # function to return ciphertext
    def encrypt(message, key):

        try:
            
            # create new ARC4 cipher
            try:
            
                obj = ciphers_stream[1].new(key.encode('utf-8'))
        
            except Exception:
            
                obj = ciphers_stream[1].new(key)
            
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
            try:
            
                obj = ciphers_stream[x].new(key.encode('utf-8'))
        
            except Exception:
            
                obj = ciphers_stream[x].new(key)            
            
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

    # function to return valid key size
    def get_valid_key_size():

        return [32]
        
    # function to return ciphertext
    def encrypt(message, secret):
        
        obj = create_instance_2(2, secret, None)
        cipher_text = get_cipher_text(obj, message)
        return cipher_text

    # function to decrypt ciphertext
    def decrypt(msg, secret):        
        
        try:

            msg_nonce = msg[:8]
            cipher_text = msg[8:]
            obj = create_instance_2(2, secret, msg_nonce)            

        except Exception:

            msg_nonce = msg[:16]
            cipher_text = msg[16:]
            obj = create_instance_2(2, secret, msg_nonce)
                
        return get_original_message(obj, cipher_text)        

"""
ChaCha20
BLOCK_SIZE = 1
KEY_SIZE = 32
"""
class chacha20(object):

    # function to return valid key size
    def get_valid_key_size():

        return [32]

    # function to return ciphertext
    def encrypt(message, secret):
        
        obj = create_instance_2(3, secret, None)
        cipher_text = get_cipher_text(obj, message)
        return cipher_text

    # function to decrypt ciphertext
    def decrypt(msg, secret):        
        
        msg_nonce = msg[:8]
        cipher_text = msg[8:]
        obj = create_instance_2(2, secret, msg_nonce)
        return get_original_message(obj, cipher_text)      
