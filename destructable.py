import pygame
import drawer

class Destructable(object):
	def __init__(self, screenPosition, anim, image):
		self.hits = 0
		self.screenPosition = screenPosition
		self.lastHit = 0
		self.anim = anim
		self.image = image
		pass

	def hitDelay(self):
		return pygame.time.get_ticks() - self.lastHit > 100

	def hit(self):
		if (self.hits < self.anim.numFrames):
			self.hits += 1
			self.lastHit = pygame.time.get_ticks()
			return self.getHighScore()
		return 0

	def getScreenPosition(self):
		return self.screenPosition

	def getHighScore(self):
		return (self.hits + 1) * 100

	def drawDestructable(self, screen):
		if (self.hits < self.anim.numFrames):
			n = self.hits
			self.anim.currentFrameNum = n
			drawer.drawAnim(self.image, self.anim, screen, self.getScreenPosition())