import character
import constants
import pyganim
import pygame, sys
from pygame.locals import *
import drawer

class Player(character.Character):
	def __init__(self, screenPosition, image, anim, world):
		character.Character()
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(screenPosition), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
		self.anim = anim
		self.image = image

	def move(self, deltaP):
		self.physicsBody.ApplyLinearImpulse(deltaP, self.physicsBody.position, True)

	def drawCharacter(self, screen, screenPosition):
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[K_a] or keys_pressed[K_d] or keys_pressed[K_w] or keys_pressed[K_s]:
			self.anim.play()
		else:
			self.anim.pause()
			self.anim.currentFrameNum = 0
		drawer.drawImage(self.image, self.anim, screen, screenPosition)
