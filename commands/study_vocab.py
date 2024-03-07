import json
import os
import random

from command_base import Command


class study_vocab(Command):
	def __init__(self):
		name = 'study'
		prefix = 'study'
		help_text = 'Starts a study session for a study set'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
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

		words = list(word_list.keys())
		random.shuffle(words)  # Shuffle for variety

		for word in words:
			print(f"\nWord: {word}")
			answer = input("Definition: ")
			if answer.lower() == word_list[word]["definition"].lower():
				print("Correct!")
				word_list[word]["score"] += 1
			else:
				print(f"Incorrect. The correct definition is: {word_list[word]['definition']}")
				word_list[word]["score"] -= 1

		with open(file_path, 'w') as file:
			json.dump(word_list, file, indent=4)

		print("\nStudy session complete!")
