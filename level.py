
class Level:
	def __init__(self, player):
		print "hej"
		self.player = player
		self.victims = []
		self.doors = []
		self.bodies = []

	def debugDraw(self, screen):
		self.player.debugDraw(screen)

	def draw(self, screen):
		self.player.draw(screen)

	def movePlayer(self, deltaP):
		self.player.move(deltaP)
