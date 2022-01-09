""" IMPORTS """


import sqlite3


""" FUNCSTIONS """


def open_con(database_name):
	con = sqlite3.connect(f"{database_name}.db")
	cur = con.cursor()

	return [con, cur]


""" MAIN """


def main():
	open_con("nero_was_nasty")



""" runs main if it's not imported """


if (__name__ == '__main__'):
	main()