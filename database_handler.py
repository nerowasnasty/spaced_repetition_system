""" IMPORTS """

	
import sqlite3


""" FUNCSTIONS """


def open_con(database_name):
	con = sqlite3.connect(f"{database_name}.db")
	cur = con.cursor()

	return [con, cur]


def create_table_creation_values_command(table_values):
	table_values_command = ""

	for key in table_values:
		if (table_values_command):
			table_values_command = f"{table_values_command}, {key} {table_values[key]}"

		else:
			table_values_command = f"{key} {table_values[key]}"

	return table_values_command


def create_columns_command(table_values):
	columns_command = ""

	for key in table_values:
		if (columns_command):
			columns_command = f"{columns_command}, {key}"

		else:
			columns_command = f"{key}"

	return columns_command


def create_values_command(table_values):
	table_values_command = ""

	for key in table_values:
		if (table_values_command):
			table_values_command = f"{table_values_command}, ?"

		else:
			table_values_command = f"?"

	return table_values_command


def create_table(con, cur, table_name, table_values):
	cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({table_values})""")
	con.commit()
	con.close()


def convert_file_to_blob(file):
	with open(file, "rb") as file:
		blob_data = file.read()

		return blob_data


def insert_into_database(con, cur, table_name, columns, table_values_command, table_values):
	cur.execute(f"""INSERT INTO {table_name}({columns}) VALUES ({table_values_command})""", table_values)
	con.commit()
	con.close()


def create_fields_command(fields):
	fields_command = ""

	for key in fields.keys():
		if (fields_command):
			fields_command = f"{fields_command} AND {key} = ?"

		else:
			fields_command = f"{key} = ?"

	return fields_command


def show_table(con, cur, table_name):
	cur.execute(f"""SELECT * FROM {table_name}""");
	results = cur.fetchall()

	con.commit()
	con.close()

	return results


def search_by_fields(con, cur, table_name, fields_command, fields):
	cur.execute(f"""SELECT * FROM {table_name} WHERE {fields_command}""", list(fields.values()))

	results = cur.fetchall()

	con.commit()
	con.close()

	return results


def show_results(results):
	for result in results:
		print(result)


def delete_by_fields(con, cur, table_name, fields_command, fields):
	cur.execute(f"""DELETE FROM {table_name} WHERE {fields_command}""", list(fields.values()))
	con.commit()
	con.close()


def create_fields_update_command(fields):
	fields_command = ""

	for key in fields.keys():
		if (fields_command):
			fields_command = f"{fields_command}, {key} = ?"

		else:
			fields_command = f"{key} = ?"

	return fields_command


def update_by_fields(con, cur, table_name, fields_update_command, fields_command, update_fields, fields):
	cur.execute(f"""UPDATE  {table_name} SET {fields_update_command}  WHERE {fields_command}""", [*list(update_fields.values()), *list(fields.values())])
	con.commit()
	con.close()


""" MAIN """


def main():
	[con, cur] = open_con("nero_was_nasty")
	create_table(con, cur, "nerowasnasty", create_table_creation_values_command({"name": "text", "age": "INTEGER", "money": "REAL", "picture": "BLOB"}))
	[con, cur] = open_con("nero_was_nasty")
	insert_into_database(con, cur, "nerowasnasty", create_columns_command({"name": "nero", "age": 19, "money": 1305805.35, "picture": convert_file_to_blob("C:\\Users\\nero\\projects\\image.jpg")}), create_values_command({"name": "nero", "age": 19, "money": 1305805.35, "picture": convert_file_to_blob("C:\\Users\\nero\\projects\\image.jpg")}), ["nero", 19, 1305805.35, convert_file_to_blob("C:\\Users\\nero\\projects\\image.jpg")])
	[con, cur] = open_con("nero_was_nasty")
	show_results(show_table(con, cur, "nerowasnasty"))
	#[con, cur] = open_con("nero_was_nasty")
	#delete_by_fields(con, cur, "nerowasnasty", create_fields_command({"name": "nero", "age": 19}), {"name": "nero", "age": 19})
	[con, cur] = open_con("nero_was_nasty")
	update_by_fields(con, cur, "nerowasnasty", create_fields_update_command({"name": "dclxvi", "age": 21}), create_fields_command({"name": "nero", "age": 19}), {"name": "dclxvi", "age": 21}, {"name": "nero", "age": 19})
	[con, cur] = open_con("nero_was_nasty")
	show_results(show_table(con, cur, "nerowasnasty"))


""" runs main if it's not imported """


if (__name__ == '__main__'):
	main()
