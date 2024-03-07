import pkgutil
import time

import commands
import commands.reverse
import commands.help
import commands.search
import commands.notes_delete


SPEED_TESTING = True

command_list = []

# # Iterate over all modules in the 'commands' package
for importer, modname, _ in pkgutil.iter_modules(commands.__path__):
	# Import the module
	module = importer.find_module(modname).load_module(modname)
	# Instantiate the class (assuming it has the same name as the module)
	command_class = getattr(module, modname)
	command_list.append(command_class())

logo = """
                                                  __                  __                               
                                                  /  |                /  |                              
  _______  __    __   ______    ______    ______  $$ |____    ______  $$ |  ______    ______    ______  
 /       |/  |  /  | /      \  /      \  /      \ $$      \  /      \ $$ | /      \  /      \  /      \ 
/$$$$$$$/ $$ |  $$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |$$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |
$$      \ $$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ $$ |  $$ |$$    $$ |$$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
 $$$$$$  |$$ \__$$ |$$ |__$$ |$$$$$$$$/ $$ |      $$ |  $$ |$$$$$$$$/ $$ |$$ |__$$ |$$$$$$$$/ $$ |      
/     $$/ $$    $$/ $$    $$/ $$       |$$ |      $$ |  $$ |$$       |$$ |$$    $$/ $$       |$$ |      
$$$$$$$/   $$$$$$/  $$$$$$$/   $$$$$$$/ $$/       $$/   $$/  $$$$$$$/ $$/ $$$$$$$/   $$$$$$$/ $$/       
                    $$ |                                                  $$ |                          
                    $$ |                                                  $$ |                          
                    $$/                                                   $$/                              
"""

if __name__ == '__main__':
	# Print the logo
	for i in range(0, len(logo), 15):
		chunk = logo[i:i + 15]
		print(chunk, end='')
		if not SPEED_TESTING:
			time.sleep(0.001)

	print('Welcome to the command line interface!')
	print('Type "help" for a list of commands')

	while True:
		input_data = input(': ')

		# figure out prefix
		for cmd in command_list:
			if input_data[:len(cmd.prefix)] != cmd.prefix:
				continue

			# remove the prefix from the input data
			input_data = input_data[len(cmd.prefix):]

			# we have the right command, execute it with input data
			cmd.execute(input_data)
