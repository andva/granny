import pygame, sys
from pygame.locals import *

class SoundManager:
	click = 0

	def __init__(self):
		SoundManager.click = pygame.mixer.Sound('sounds/click.wav')

	def playClick(self):
		SoundManager.click.play()
