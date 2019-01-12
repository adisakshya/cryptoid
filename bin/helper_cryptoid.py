"""
MODULE NAME: helper_cryptoid
Author: Adisakshya Chauhan
"""

from lists import list_symmetric_ciphers, list_asymmetric_ciphers
import codecs
from Crypto.Random import get_random_bytes

op_formats = ["", "base64", "hex"]

def valid_key_size(cipher_no):

	return list_symmetric_ciphers[cipher_no].get_valid_key_size()

def transform(cipher_text, op_format_no):

	return codecs.encode(cipher_text, op_formats[op_format_no]).decode('utf-8')

def get_sym_cipher_text(message, cipher_no, mode_no=1, 
			iv="This is an IV456", key="This is a key123", 
			op_format_no=1):

	print("\nEncrypting message: ",message)
	print("With ", list_symmetric_ciphers[cipher_no])
	
	cipher_text = " "

	# symmetric cipher
	cipher = list_symmetric_ciphers[cipher_no]
		
	# call to appropriate cipher
	try:
		
		try:

			cipher_text = cipher.encrypt(message, key, mode_no, iv)
		
		except:

			cipher_text = cipher.encrypt(message, key, mode_no)
	
	except TypeError:
		
		cipher_text = cipher.encrypt(message, key)

	try:
		return transform(cipher_text, op_format_no)
	except:
		print('Nope')
		return cipher_text

def get_asym_cipher_text(cipher_no, message, key=None, 
							shift_count=0, op_format_no = 1):
	
	cipher_no -= 9
	print("\nEncrypting message: ",message)
	print("With ",list_asymmetric_ciphers[cipher_no])
	if key:
		print("Key: ", key)
	else:
		print("Shift Count: ", shift_count)

	if cipher_no == 1:

		public_key = key.publickey()
		cipher_text = list_asymmetric_ciphers[cipher_no].encrypt(public_key, message)

	if cipher_no == 2:

		cipher_text = list_asymmetric_ciphers[cipher_no].encrypt(message, key)
	
	if cipher_no == 3:

		cipher_text = list_asymmetric_ciphers[cipher_no].encrypt(message, shift_count)
	
	if cipher_no in [2, 5, 6]:

		cipher_text = list_asymmetric_ciphers[cipher_no].encrypt(message)
	
	try:
		return transform(cipher_text, op_format_no)
	except:
		return cipher_text


def get_mode():

	print("Select operating mode\n\t\t1. Encryption\n\t\t2. Decryption")
	return int(input('-> '))

def get_key(cipher_no, valid_key_size_list):

	print("\nValid key size(s): ", valid_key_size_list)
	choice = input("Want a auto-generated key? (Y/N): ")

	if choice in ['y', 'Y']:

		return get_random_bytes(valid_key_size_list[0])

	else:

		return input("Enter key: ")	

def sym_encryption(message, cipher_no):

	print("\nEnter Mode: \n\t\t1. ECB\n\t\t2. CBC\n\t\t3. CFB\n\t\t4. OFB\n\t\t5. CTR\n\t\t6. EAX")
	mode_no = int(input('\nEnter mode number -> '))

	iv = "This is an IV456"
	if mode_no in range(2,6):
		
		iv = input("\nEnter initialization vector: ")

	key = get_key(cipher_no, valid_key_size(cipher_no))

	print("\nEnter Encrypted output fromat: \n\t\t1.BASE64\n\t\t2. HEX")
	op_format_no = int(input('\nEnter choice: '))

	return get_sym_cipher_text(message, cipher_no, mode_no, iv, key, op_format_no)	

def asym_encryption(message, cipher_no):
	
	key = None
	shift_count = 0

	if cipher_no == 10:

		print("Generating RSA key...")
		key = list_asymmetric_ciphers[cipher_no-9].generate_rsa_keys(1024)
		print("Generated RSA key: ", key, key.publickey())
	
	elif cipher_no == 12:

		print("Enter Shift Count: ")
		shift_count = int(input())
	
	if cipher_no not in [10, 12]:

		print("Enter secret key: ")
		key = input()	
	
	print("Enter Encrypted output fromat: \n\t\t1. BASE64\n\t\t2. HEX")
	op_format_no = int(input())

	cipher_text = get_asym_cipher_text(cipher_no, message, key, shift_count, op_format_no)	

	return cipher_text
