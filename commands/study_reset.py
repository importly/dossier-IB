import json
import os
from command_base import Command


class study_reset(Command):
	def __init__(self):
		name = 'reset_studyset'
		prefix = 'rs'
		help_text = 'Resets the scores of a study set'
		super().__init__(name, prefix, help_text)

def execute(self, input_data):
	# Implement the reset logic here
	set_name = input_data.strip()
	if not set_name:
		print("Error: Please provide a study set name.")
		return

	file_path = f"{set_name}.json"
	if not os.path.exists(file_path):
		print(f"Error: Study set '{set_name}' not found.")
		return

	with open(file_path, 'r') as file:
		word_list = json.load(file)

	for word in word_list:
		word_list[word]["score"] = 0

	with open(file_path, 'w') as file:
		json.dump(word_list, file, indent=4)

	print(f"Study set '{set_name}' scores reset successfully!")