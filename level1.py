from level import Level
from player import Player
from wall import Wall
import constants

class Level1(Level):
	def __init__(self, world):
		self.player = Player((100,100), world)
		self.walls = [
			#screenPos, Size
			Wall((100, 40), (100,10), world),
			#Wall((3,0), (1,20), world)
			]

		Level(self.player)
