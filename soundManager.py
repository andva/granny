import pygame, sys
from pygame.locals import *

class SoundManager:
	cane = 0

	def __init__(self):
		SoundManager.cane = pygame.mixer.Sound('sounds/cane.wav')

	def playCane(self):
		SoundManager.cane.play()
