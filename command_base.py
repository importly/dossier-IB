class Command:
	def __init__(self, name, prefix, help_text):
		self.name = name
		self.prefix = prefix
		self.help_text = help_text

	def execute(self, input_data: str):
		pass
