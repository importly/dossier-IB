

import json
import os

from command_base import Command

class notes_delete(Command):
	def __init__(self):
		name = 'deletenote'
		prefix = 'dn'
		help_text = 'deletes a note'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		notes_dir = 'notes'

		if not os.path.exists(notes_dir):
			os.makedirs(notes_dir)  # Create the folder if needed

		title = input("Enter note title: ")
		content = input("Enter note content: ")

		note_data = {
			"title": title,
			"content": content
		}

		filename = f"{title}.json"  #  Example filename strategy
		filepath = os.path.join(notes_dir, filename)

		with open(filepath, 'w') as file:
			json.dump(note_data, file)

		print(f"Note '{title}' created successfully!")
