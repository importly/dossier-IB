import json
import os

from command_base import Command


class study_create(Command):
	def __init__(self):
		name = 'create_studyset'
		prefix = 'cs'
		help_text = 'Creates a new study set'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		set_name = input_data.strip()
		if not set_name:
			print("Error: Please provide a name for the study set.")
			return

		file_path = f"{set_name}.json"
		if os.path.exists(file_path):
			print(f"Error: Study set '{set_name}' already exists.")
			return

		word_list = {}
		print("Enter words and their definitions (type 'done' when finished):")
		while True:
			word = input("Word: ")
			if word.lower() == 'done':
				break
			definition = input("Definition: ")
			word_list[word] = {"definition": definition, "score": 0}

		with open(file_path, 'w') as file:
			json.dump(word_list, file, indent=4)

		print(f"Study set '{set_name}' created successfully!")