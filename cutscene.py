import pygame, sys
from pygame.locals import *
import drawer
import viewManager

class Cutscene:

	image = 0
	i = 0
	id = 0
	img = 0
	type = 'cutscene'

	def __init__(self, image, id):
		self.image = image
		self.id = id
		self.img = pygame.image.load(self.image).convert()

	def draw(self, screen):
		d = pygame.time.get_ticks() % 1
		if(d == 0 and self.i > -720):
			self.i -= 2
		drawer.drawImage(self.img, screen, (0,self.i))

	def debugDraw(self, screen):
		pass

	def movePlayer(self, deltaP):
		pass

	def update(self, world):
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[K_SPACE]:
			viewManager.loadLevel(self.id, world)
