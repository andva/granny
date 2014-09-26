from level import Level
from player import Player
from wall import Wall
import constants

class Level1(Level):
	def __init__(self, world):
		self.player = Player((100,100), 'images/granny.png', world)
		midx = constants.SCREEN_WIDTH / 2.0
		midy = constants.SCREEN_HEIGHT / 2.0

		self.player = Player((midx,midy), 'images/granny.png', world)
		self.walls = [
			#screenPos, Size
			#Wall((midx, midy - 200), (200,10), world),
			Wall((midx - 200, midy), (10,100), world),
			Wall((midx + 200, midy), (10,100), world),
			]

		Level(self.player)
