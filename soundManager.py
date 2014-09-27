import pygame, sys
from pygame.locals import *

class SoundManager:
	cane = 0
	breaking = 0

	def __init__(self):
		SoundManager.cane = pygame.mixer.Sound('sounds/cane.wav')
		SoundManager.breaking = pygame.mixer.Sound('sounds/breaking.wav')

	def playCane(self):
		SoundManager.cane.play()

	def playBreaking(self):
		SoundManager.breaking.play()
