# Code obfuscator
def encrypt(text: str, key: any) -> str:
	cipher_text = ""
	ascii_text = [ord(char) for char in text]
	for char in ascii_text:
		cipher_text += chr(char^key)
	return cipher_text

def decrypt(text: str, key: any) -> str:
	plain_text = ""
	ascii_text = [ord(char) for char in text]
	for char in ascii_text:
		plain_text += chr(char^key)
	return plain_text

def frequency_counter(text: str) -> dict:
	frequency = {}
	for i in text:
		if i in frequency:
			frequency[i] += 1
		else:
			frequency[i] = 1

	return frequency

if __name__ == "__main__":
	# poop = encrypt("", 283)
	# print(poop)
	# poop = decrypt(poop, 283)
	# print(poop)

	x = str(input("please enter a string: "))
	print(frequency_counter(x))
