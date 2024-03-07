from command_base import Command


class help(Command):
	def __init__(self):
		name = 'help'
		prefix = 'help'
		help_text = 'Prints the help text for all commands'
		super().__init__(name, prefix, help_text)

	def execute(self, input_data):
		from main import command_list

		for cmd in command_list:
			print(f'{cmd.prefix} - {cmd.name} - {cmd.help_text}')
