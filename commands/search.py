from command_base import Command

# this command just searches for a target value in an array using linear search


class search(Command):
	def __init__(self):
		name = 'linear_search'
		prefix = 'lin_search'
		help_text = 'Searches for a target value in an array using linear search'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		# Splitting input data into target value and array
		target, *array = input_data.strip().split(' ')
		array = [int(i) for i in array]
		target = int(target)

		# Linear search

		for i in range(len(array)):
			if array[i] == target:
				print(f"Target {target} found at position: {i}")
				return
		print(f"Target {target} not found in the array.")
