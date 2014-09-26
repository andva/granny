from level import Level
from player import Player
from wall import Wall

class Level1(Level):
	def __init__(self, world):
		self.player = Player((10,15), world)
		self.walls = [
			Wall((0,-3), (50,5), world),
			Wall((-3,0), (5,50), world)
			]

		Level(self.player)
