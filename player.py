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
		fixture = self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
		fixture.userData = self
		self.physicsBody.userData = self
		self.initialized = True

	def move(self, deltaP):
		if (self.initialized):
			self.physicsBody.ApplyLinearImpulse(deltaP, self.physicsBody.position, True)

	def drawCharacter(self, screen, screenPosition):
		keys_pressed = pygame.key.get_pressed()
		if self.anim.currentFrameNum < 10:
			if keys_pressed[K_RETURN] == False:
				if keys_pressed[K_a] or keys_pressed[K_d] or keys_pressed[K_w] or keys_pressed[K_s]:
					if keys_pressed[K_a]:
						self.left = True
					if keys_pressed[K_d]:
						self.left = False

					if self.left == True:
						if self.anim.currentFrameNum > 3:
							self.anim.currentFrameNum = 0

					if self.left == False:
						if self.anim.currentFrameNum < 5 or self.anim.currentFrameNum > 8:
							self.anim.currentFrameNum = 5
					self.anim.play()
				else:
					self.anim.pause()
					if self.left == True:
						self.anim.currentFrameNum = 0
					if self.left == False:
						self.anim.currentFrameNum = 5
			else:
				if self.left == True:
					self.anim.currentFrameNum = 10
				if self.left == False:
					self.anim.currentFrameNum = 16
				self.anim.play()
		if self.left == True:
			if self.anim.currentFrameNum > 14:
				self.anim.currentFrameNum = 0
		if self.left == False:
			if self.anim.currentFrameNum > 20:
				self.anim.currentFrameNum = 5

		drawer.drawAnim(self.image, self.anim, screen, screenPosition)
