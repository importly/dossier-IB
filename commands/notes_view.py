
import json
import os

from command_base import Command

class notes_view(Command):
	def __init__(self):
		name = 'viewnotes'
		prefix = 'vn'
		help_text = 'Displays a list of available notes'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		notes_dir = 'notes'  # Folder to store notes

		if not os.path.exists(notes_dir):
			print("Notes folder not found. Create notes using 'createnote'.")
			return

		note_files = os.listdir(notes_dir)
		if not note_files:
			print("No notes found.")
			return

		print("Available Notes:")
		for index, filename in enumerate(note_files):
			file_title = os.path.splitext(filename)[0]  # Remove .json extension
			print(f"{index + 1}. {file_title}")

		choice = input("Select a note to view (or type 'back'): ")

		try:
			if choice.lower() == 'back':
				return
			else:
				selected_index = int(choice) - 1  # Convert to 0-based index
				selected_file = note_files[selected_index]
				with open(os.path.join(notes_dir, selected_file), 'r') as file:
					note_data = json.load(file)
					print(f"\nTitle: {note_data['title']}")
					print(f"Content:\n{note_data['content']}")
		except (IndexError, ValueError, json.JSONDecodeError):
			print("Invalid choice or error reading note.")
