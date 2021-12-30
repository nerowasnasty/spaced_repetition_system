""" FUNCTIONS """


def generate_menu(menu_name, options_array):
	print(f'{menu_name}:')

	for i in range(len(options_array)):
		print(f'  [{i}] {options_array[i]}')

	print(f'  [{len(options_array) + 1}] exit')

	return input(f'choose an option[{len(options_array) + 1}]: ')


""" MAIN FUNCTION """


def main():
	print('first menu: ', generate_menu('main menu', ['show cards', 'search card', 'add card', 'remove card', 'edit card', 'show decks', 'search deck', 'add deck', 'remove deck', 'edit deck']))

	print('second menu: ', generate_menu('Hello, Eliot', ['marijuana', 'mophine', 'heroin']))


""" runs main if it's not imported """


if (__name__ == '__main__'):
	main()