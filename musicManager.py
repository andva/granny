import pygame, sys
from pygame.locals import *

class MusicManager:

	def __init__(self):
		pygame.mixer.music.load('sounds/click.wav')

	def playMusic(self):
		pygame.mixer.music.play(-1)