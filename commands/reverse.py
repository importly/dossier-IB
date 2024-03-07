from command_base import Command


class reverse(Command):
	def __init__(self):
		name = 'reverse'
		prefix = 'reverse'
		help_text = 'Reverses the order of elements in an array'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		array = [i for i in input_data.strip().split(' ')]

		# Reversing the array
		reversed_array = array[::-1]

		print("Reversed array:", reversed_array)
