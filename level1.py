from level import Level
from player import Player
from wall import Wall
from victim import Victim
import constants
import pyganim

class Level1(Level):
	def __init__(self, world, id):
		midx = constants.SCREEN_WIDTH / 2.0
		midy = constants.SCREEN_HEIGHT / 2.0
		self.id = id

		playerAnim = pyganim.PygAnimation([('images/granny.png', 0.1), ('images/granny2.png', 0.1), ('images/granny.png', 0.1), ('images/granny3.png', 0.1)])
		self.player = Player((midx,midy), 'images/granny.png', playerAnim, world)
		self.walls = [
			#screenPos, Size
			#Wall((midx, midy - 200), (200,10), world),
			Wall((midx - 200, midy), (10,100), world),
			Wall((midx + 200, midy), (10,100), world),
			]
		victimAnim = pyganim.PygAnimation([('images/granny.png', 0.1), ('images/granny2.png', 0.1), ('images/granny.png', 0.1), ('images/granny3.png', 0.1)])
		self.victims = [
			Victim((midx + 100, midy), 'images/granny.png', victimAnim, world)
		]
		Level(self.player)
