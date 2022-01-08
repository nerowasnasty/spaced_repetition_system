""" IMPORTS """


from PIL import Image


""" FUNCTIONS """


def open_image(file):
	image = Image.open(file)
	image.show()


""" MAIN """


def main():
	open_image("C:\\Users\\nero\\Downloads\\image.jpg")


""" runs main if it's not imported """


if (__name__ == '__main__'):
	main()