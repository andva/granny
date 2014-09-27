import pygame
import drawer

class Destructable(object):
	def __init__(self, screenPosition, anim, image):
		self.hits = 0
		self.screenPosition = screenPosition
		self.lastHit = 0
		self.anim = anim
		self.image = image
		self.lastScore = 0
		pass

	def hitDelay(self):
		return pygame.time.get_ticks() - self.lastHit > 800

	def hit(self):
		if (self.hits < self.anim.numFrames):
			self.hits += 1
			self.lastHit = pygame.time.get_ticks()
			self.lastScore = self.getHighScore()
			return self.lastScore
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