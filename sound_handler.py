""" IMPORTS """

import os


""" GLOBAL FUNCTIONS """


os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


""" IMPORTS """


import pygame
from pygame import mixer


""" FUNCTIONS """


def play(music):
	mixer.init()
	mixer.music.load(music)
	mixer.music.play()

	while pygame.mixer.music.get_busy(): 
		pygame.time.Clock().tick(10)


""" MAIN FUNCTIONS """


def main():
	play("C:\\Users\\nero\\Downloads\\industry_baby.mp3")


""" runs main if it's not imported """


if (__name__ == '__main__'):
	main()