import pygame

class Room:
	def __init__(self, id, screenPos, screenSize):
		self.id = id
		self.screenPos = screenPos
		self.screenSize = screenSize

	def debugDraw(self, screen):
		ad = [self.screenSize[0] / 2., self.screenSize[1] / 2.]
		vertices = [(self.screenPos[0] - ad[0], self.screenPos[1] - ad[1]),
					(self.screenPos[0] + ad[0], self.screenPos[1] - ad[1]),
					(self.screenPos[0] + ad[0], self.screenPos[1] + ad[1]),
					(self.screenPos[0] - ad[0], self.screenPos[1] + ad[1]),
					]
		pygame.draw.polygon(screen, (0, 255, 0, 1), vertices)
