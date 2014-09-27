import pygame

class ScoreEntry:
	def __init__(self, score, screenPos):
		self.score = score
		self.screenPos = screenPos
		self.time = pygame.time.get_ticks()

class HighScore:
	def __init__(self):
		self.entries = []
		self.totalScore = 0
	def addScore(self, point, screenPos):
		self.totalScore += point
		self.entries.append(ScoreEntry(point, screenPos))

	def update(self):
		newList = []
		for v in self.entries:
			if pygame.time.get_ticks() - v.time < 900:
				newList.append(v)
		self.entries = newList
		return