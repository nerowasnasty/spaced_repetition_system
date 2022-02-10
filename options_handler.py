""" FUNCTIONS """


def print_menu_option(option_number, option_text):
	""" prints "[n] option_text", where n is the option number and option_text is the option to be choose"""
	print(f'  [{option_number}] {option_text}')


def generate_menu(menu_name, options_array):
	""" prints menu name, options with numbers and exit option"""

	try:
		print(f'{menu_name}:') # menu name:

		# var declaration
		last_option = len(options_array)

		# loops through all optoins printing them
		for option_number in range(last_option):
			print_menu_option(option_number, options_array[option_number]) # [n] option text (e.g. "[1] save changes to database")

		# print exit option
		print_menu_option(last_option, "exit")

		# if everything is fine, returns true
		return True

	except:
		# if there's any mistake, returns false
		return False


def input_options(options_array, user_input):
	try:
		if (int(user_input) <= len(options_array)):
			return True

		else:
			return False

	except:
			return False


""" MAIN FUNCTION """


def main():
	print('first menu: ', generate_menu('main menu', ['show cards', 'search card', 'add card', 'remove card', 'edit card', 'show decks', 'search deck', 'add deck', 'remove deck', 'edit deck']))

	print('second menu: ', generate_menu('Hello, Eliot', ['marijuana', 'mophine', 'heroin']))

	print('input validation with 1:', input_options(['show cards', 'search card', 'add card', 'remove card', 'edit card', 'show decks', 'search deck', 'add deck', 'remove deck', 'edit deck'], '1'))

	print('input validation with a:', input_options(['show cards', 'search card', 'add card', 'remove card', 'edit card', 'show decks', 'search deck', 'add deck', 'remove deck', 'edit deck'], 'a'))

	print('input validation with 11:', input_options(['show cards', 'search card', 'add card', 'remove card', 'edit card', 'show decks', 'search deck', 'add deck', 'remove deck', 'edit deck'], '11'))

	print('input validation with 12:', input_options(['show cards', 'search card', 'add card', 'remove card', 'edit card', 'show decks', 'search deck', 'add deck', 'remove deck', 'edit deck'], '12'))


""" runs main if it's not imported """


if (__name__ == '__main__'):
	main()
