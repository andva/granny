import character
import constants
import pyganim
import pygame, sys
from pygame.locals import *
import drawer

class Player(character.Character):

	left = True

	def __init__(self, screenPosition, image, anim, world):
		super(Player, self).__init__()
		self.anim = anim
		self.image = image
		self.startPositionScreen = screenPosition

	def addPhysics(self, world):
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(self.startPositionScreen), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
		self.initialized = True

	def move(self, deltaP):
		if (self.initialized):
			self.physicsBody.ApplyLinearImpulse(deltaP, self.physicsBody.position, True)

	def drawCharacter(self, screen, screenPosition):
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[K_a] or keys_pressed[K_d] or keys_pressed[K_w] or keys_pressed[K_s]:
			if keys_pressed[K_a]:
				self.left = True
			if keys_pressed[K_d]:
				self.left = False
				print("False")

			if self.left == True:
				print("True")
				if self.anim.currentFrameNum > 3:
					print("is")
					self.anim.currentFrameNum = 0
					print("good")

			if self.left == False:
				print("is")
				if self.anim.currentFrameNum < 4 or self.anim.currentFrameNum > 7:
					print("good")
					self.anim.currentFrameNum = 4
			self.anim.play()
		else:
			self.anim.pause()
			if self.left == True:
				self.anim.currentFrameNum = 0
			if self.left == False:
				self.anim.currentFrameNum = 4

		drawer.drawAnim(self.image, self.anim, screen, screenPosition)
