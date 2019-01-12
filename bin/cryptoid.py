"""
MODULE NAME: cryptoid
Author: Adisakshya Chauhan
"""

from helper import *

def encryption():

	message = input('Enter Input Text: ')

	print("Select Cipher: \n\t\t1. AES\n\t\t2. DES\n\t\t3. Triple DES\n\t\t4. RC2\n\t\t5. CAST\n\t\t6. Blowfish\n\t\t7. RC4\n\t\t8. Salsa20\n\t\t9. ChaCha20")
	print("\n\t\t10. RSA\n\t\t11. Viginere Cipher\n\t\t12. Caesar Cipher\n\t\t13. --Playfair Cipher--\n\t\t14. Square Cipher\n\t\t15. --Serpant--")
	cipher_no = int(input('\nEnter cipher number -> '))

	cipher_text = None
	if cipher_no in range(1,10):

		cipher_text = sym_encryption(message, cipher_no)

	else:

		cipher_text = asym_encryption(message, cipher_no)
			
	print("Cipher-Text: ",cipher_text)

def decryption():
	
	pass	

def main():

	operating_mode = get_mode()

	if operating_mode == 1:

		encryption()

	else:

		decryption()	


if __name__ == '__main__':
	
	main()
