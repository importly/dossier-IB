from command_base import Command


class bubble(Command):
	def __init__(self):
		name = 'bubble'
		prefix = 'bubble'
		help_text = 'Sorts an array of integers using bubble sort'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		input_data = input_data.strip().split(' ')

		input_data = [int(i) for i in input_data]
		if not all(isinstance(i, int) for i in input_data):
			print("Error: Input must be a list of integers.")
			return

		# Bubble sort algorithm
		n = len(input_data)
		for i in range(n):
			for j in range(0, n - i - 1):
				if input_data[j] > input_data[j + 1]:
					input_data[j], input_data[j + 1] = input_data[j + 1], input_data[j]  # Swap

		print("Sorted array:", input_data)
