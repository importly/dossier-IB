import json
import os

from command_base import Command


class homework_add(Command):
	def __init__(self):
		name = 'add_homework'
		prefix = 'addhw'
		help_text = 'Adds a new homework entry to homework.json file'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		homework_details = input_data.strip().split(';')
		if len(homework_details) != 3:
			print("Error: Incorrect number of arguments. Expected format: title;description;due_date")
			return

		# Parsing homework details
		homework_entry = {
			"title": homework_details[0],
			"description": homework_details[1],
			"due_date": homework_details[2]
		}

		# File path
		file_path = 'homework.json'

		# Check if homework.json exists and read its content
		if os.path.exists(file_path):
			with open(file_path, 'r') as file:
				try:
					data = json.load(file)
					if not isinstance(data, list):
						data = []
				except json.JSONDecodeError:
					data = []
		else:
			data = []

		# Append new homework entry to data
		data.append(homework_entry)

		# Write updated data back to homework.json
		with open(file_path, 'w') as file:
			json.dump(data, file, indent=4)

		print(f"Added new homework: {homework_entry['title']}")
