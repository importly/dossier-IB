import hashlib

from command_base import Command


class hash(Command):
	def __init__(self):
		name = 'hash'
		prefix = 'hash'
		help_text = ('Encodes input data to a specified SHA hash. Supports SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, '
		             'SHA3-224, SHA3-256, SHA3-384, SHA3-512.')
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		try:
			hash_type, text = input_data.split(' ', 1)
		except ValueError:
			print("Error: Please specify the hash type followed by the text to hash.")
			return

		hash_function = None

		# Using if-elif statements to match the hash type
		if hash_type.upper() == 'SHA-1':
			hash_function = hashlib.sha1
		elif hash_type.upper() == 'SHA-224':
			hash_function = hashlib.sha224
		elif hash_type.upper() == 'SHA-256':
			hash_function = hashlib.sha256
		elif hash_type.upper() == 'SHA-384':
			hash_function = hashlib.sha384
		elif hash_type.upper() == 'SHA-512':
			hash_function = hashlib.sha512
		elif hash_type.upper() == 'SHA3-224':
			hash_function = hashlib.sha3_224
		elif hash_type.upper() == 'SHA3-256':
			hash_function = hashlib.sha3_256
		elif hash_type.upper() == 'SHA3-384':
			hash_function = hashlib.sha3_384
		elif hash_type.upper() == 'SHA3-512':
			hash_function = hashlib.sha3_512

		if hash_function is None:
			print(
				f"Error: Unsupported hash type '{hash_type}'. Available types are: SHA-1, SHA-224, SHA-256, SHA-384, "
				f"SHA-512, SHA3-224, SHA3-256, SHA3-384, SHA3-512.")
			return

		# Generating the hash
		hash_object = hash_function(text.encode())
		hex_dig = hash_object.hexdigest()

		print(f"{hash_type} hash of '{text}': {hex_dig}")
