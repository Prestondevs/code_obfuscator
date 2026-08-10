# Code obfuscator
def encrypt(text: str, key: any):
	cipher_text = ""
	ascii_text = [ord(char) for char in text]
	for char in ascii_text:
		cipher_text += chr(char^key)
	return cipher_text

def decrypt(text: str, key: any):
	plain_text = ""
	ascii_text = [ord(char) for char in text]
	for char in ascii_text:
		plain_text += chr(char^key)
	return plain_text


if __name__ == "__main__":
	poop = encrypt("hello", 12)
	print(poop)
	poop = decrypt(poop, 12)
	print(poop)