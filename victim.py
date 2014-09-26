import character
import constants
import pyganim
import pygame, sys
from pygame.locals import *
import drawer

class Victim(character.Character):
	def __init__(self, screenPosition, image, anim, world):
		self.screenPosition = screenPosition
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(screenPosition), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
		self.anim = anim
		self.image = image

	def draw(self):
		print "hej"

	def drawCharacter(self, screen, screenPosition):
		self.anim.pause()
		drawer.drawImage(self.image, self.anim, screen, screenPosition)