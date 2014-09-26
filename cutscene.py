import pygame, sys
from pygame.locals import *
import drawer
import viewManager

class Cutscene:

	image = 0
	i = 0
	id = 0

	def __init__(self, image, id):
		self.image = image
		self.id = id

	def draw(self, screen):
		d = pygame.time.get_ticks() % 1
		if(d == 0):
			self.i -= 3
		drawer.drawImage(self.image, screen, (0,self.i))

	def movePlayer(self, deltaP):
		pass

	def update(self):
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[K_SPACE]:
			viewManager.loadLevel(self.id)
