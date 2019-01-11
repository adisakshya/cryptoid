"""
MODULE NAME: cryptoid
Author: Adisakshya Chauhan
"""

from helper import get_sym_cipher_text, valid_key_size

def get_mode():

	print("Select operating mode\n\t\t1. Encryption\n\t\t2. Decryption")
	return int(input())

def sym_encryption(message, cipher_no):

	print("Enter Mode: \n\t\t1. ECB\n\t\t2. CBC\n\t\t3. CFB\n\t\t4. OFB\n\t\t5. CTR\n\t\t6. EAX")
	mode_no = int(input())

	iv = "This is an IV456"
	if mode_no in range(2,6):
		
		print("Enter initialization vector: ")
		iv = input()

	print("Enter secret key: (valid size: ",valid_key_size(cipher_no),")")
	key = input()

	print("Enter Encrypted output fromat: \n\t\t1.BASE64\n\t\t2. HEX")
	op_format_no = int(input())

	encrypted_text = get_sym_cipher_text(message, cipher_no, mode_no, iv, key, op_format_no)
	return encrypted_text	

def asym_encryption(message, cipher_no):
	
	pass		

def encryption():

	print("Enter Input Text: ")
	message = input()

	print("Select Cipher: \n\t\t1. AES\n\t\t2. DES\n\t\t3. Triple DES\n\t\t4. RC2\n\t\t5. CAST\n\t\t6. Blowfish\n\t\t7. RC4\n\t\t8. Salsa20\n\t\t9. ChaCha20")
	#print("\n\t\t10. RSA\n\t\t11. Viginere Cipher\n\t\t12.Caesar Cipher\n\t\t13.Playfair Cipher\n\t\t14. Square Cipher\n\t\t15. Serpant")
	cipher_no = int(input())

	cipher_text = None
	if cipher_no in range(1,10):

		cipher_text = sym_encryption(message, cipher_no)

	else:

		cipher_text = asym_encryption(message, cipher_no)		
	print(cipher_text)

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
