"""
MODULE NAME: cryptoid
Author: Adisakshya Chauhan
"""

from helper_cryptoid import *

def encryption():

	message = input('Enter Input Text: ')

	cipher_no = get_cipher()

	cipher_text = None
	if cipher_no in range(1,10):

		cipher_text = sym_encryption(message, cipher_no)

	else:

		cipher_text = asym_encryption(message, cipher_no)
			
	print("Cipher-Text: ",cipher_text)
	save_result(cipher_text)

def decryption():
	
	if input('Have a file with ciphertext? (Y/N): ') in ['y', 'Y']:
		file_name = input('Enter file name:(with extension) ')
		f = open(filename, 'r')
		cipher_text = f.read()
	else:
		cipher_text = input('Enter cipher-text: ')

	cipher_no = get_cipher()	
	if cipher_no in range(1,10):

		message = sym_decryption(cipher_text, cipher_no)

	else:

		message = asym_decryption(cipher_text, cipher_no)	

	print('Message: ', message)
	save_result(cipher_text)

def main():

	operating_mode = get_mode()

	if operating_mode == 1:

		encryption()

	else:

		decryption()	


if __name__ == '__main__':
	
	main()
