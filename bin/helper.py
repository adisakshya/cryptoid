"""
MODULE NAME: helper
Author: Adisakshya Chauhan
"""
from lists import list_symmetric_ciphers, list_asymmetric_ciphers

def valid_key_size(cipher_no):

	return list_symmetric_ciphers[cipher_no].get_valid_key_size()

def get_sym_cipher_text(message, cipher_no, mode_no=1, 
			iv="This is an IV456", key="This is a key123", 
			op_format_no=1):

	cipher_text = " "

	# symmetric cipher
	cipher = list_symmetric_ciphers[cipher_no]
		
	# call to appropriate cipher
	try:
		
		cipher_text = cipher.encrypt(message, key, mode_no, iv)
	
	except Exception:
		
		cipher_text = cipher.encrypt(message, key, mode_no)

	return cipher_text