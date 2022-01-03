""" FUNCTIONS """


def generate_menu(menu_name, options_array):
	print(f'{menu_name}:')

	for i in range(len(options_array)):
		print(f'  [{i}] {options_array[i]}')

	print(f'  [{len(options_array) + 1}] exit')

	return input(f'choose an option[{len(options_array) + 1}]: ')


def input_options(options_array, user_input):
		try:
			if (int(user_input) <= len(options_array) + 1):
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
