# Code obfuscator
ciphertext = "@_:\x15\x05C:\x01\x01EERF\\rPW@=)\x02\x19\r\x19\x06CWrVJDCEF-\x08\x0c\x056\x07\x14nQ\\[U\x19"


def encrypt(text, key) -> str:
	cipher_text = ""
	# accept `text`/`key` as bytes OR as ascii/str normalize to code points either way
	ascii_text = list(text) if isinstance(text, (bytes, bytearray)) else [ord(char) for char in text]
	key_codes = list(key) if isinstance(key, (bytes, bytearray)) else [ord(char) for char in key]
	for i, char in enumerate(ascii_text):
		cipher_text += chr(char ^ key_codes[i % len(key_codes)])
	return cipher_text


def decrypt(text, key) -> str:
	plain_text = ""
	ascii_text = list(text) if isinstance(text, (bytes, bytearray)) else [ord(char) for char in text]
	key_codes = list(key) if isinstance(key, (bytes, bytearray)) else [ord(char) for char in key]
	for i, char in enumerate(ascii_text):
		plain_text += chr(char ^ key_codes[i % len(key_codes)])
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
	# x = str(input("please enter a string: "))
	# print(frequency_counter(x))
	decrypted = decrypt(ciphertext, "$%Yacking1234901")
	print(f"Decrypted: {decrypted}")
