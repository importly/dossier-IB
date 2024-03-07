import json
import os

from command_base import Command


class homework_remove(Command):
	def __init__(self):
		name = 'remove_homework'
		prefix = 'rmhw'
		help_text = 'Removes a homework entry from homework.json file by its title'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		homework_title = input_data.strip()

		# File path
		file_path = 'homework.json'

		# Ensure the homework.json file exists
		if not os.path.exists(file_path):
			print("Error: homework.json file does not exist.")
			return

		# Read current homework entries
		with open(file_path, 'r') as file:
			try:
				data = json.load(file)
				if not isinstance(data, list):
					print("Error: homework.json content is invalid.")
					return
			except json.JSONDecodeError:
				print("Error: homework.json is not in valid JSON format.")
				return

		# Filter out the homework entry to remove
		updated_data = [entry for entry in data if entry['title'] != homework_title]

		if len(updated_data) == len(data):
			print(f"No homework found with the title '{homework_title}'. No changes made.")
			return

		# Write the updated data back to homework.json
		with open(file_path, 'w') as file:
			json.dump(updated_data, file, indent=4)

		print(f"Removed homework: {homework_title}")
