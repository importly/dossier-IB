import json
import os

from command_base import Command


class homework_view(Command):
	def __init__(self):
		name = 'view_homework'
		prefix = 'viewhw'
		help_text = 'Displays all homework entries'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		file_path = 'homework.json'

		if not os.path.exists(file_path):
			print("No homework entries found.")
			return

		with open(file_path, 'r') as file:
			try:
				data = json.load(file)
			except json.JSONDecodeError:
				print("Error: Invalid homework data.")
				return

		if not data:
			print("No homework entries found.")
			return

		print("Homework Assignments:")
		for index, entry in enumerate(data):
			print(f"{index + 1}. Title: {entry['title']}")
			print(f"   Description: {entry['description']}")
			print(f"   Due Date: {entry['due_date']}\n")

