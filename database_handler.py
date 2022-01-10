""" IMPORTS """


import sqlite3


""" FUNCSTIONS """


def open_con(database_name):
	con = sqlite3.connect(f"{database_name}.db")
	cur = con.cursor()

	return [con, cur]


def create_values_command(table_values):
	table_values_command = ""

	for key in table_values:
		if (table_values_command):
			table_values_command = f"{table_values_command}, {key} {table_values[key]}"

		else:
			table_values_command = f"{key} {table_values[key]}"

	return table_values_command


def create_table(con, cur, table_name, table_values):
	cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({table_values})""")
	con.commit()
	con.close()


def convert_file_to_blob(file):
	with open(file, "rb") as file:
		blob_data = file.read()

		return blob_data


""" MAIN """


def main():
	[con, cur] = open_con("nero_was_nasty")
	create_table(con, cur, "nerowasnasty", create_values_command({"name": "text", "age": "INTEGER", "money": "REAL", "picture": "BLOB"}))
	print(convert_file_to_blob("C:\\Users\\nero\\projects\\quer_voar_industry_baby.mp3"))



""" runs main if it's not imported """


if (__name__ == '__main__'):
	main()
