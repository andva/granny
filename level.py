import drawer

class Level:

	id = 0
	image = 0
	img = 0
	type = 'level'

	def __init__(self, player):
		print "hej"
		self.player = player
		self.victims = []
		self.doors = []
		self.bodies = []


	def debugDraw(self, screen):
		self.player.debugDraw(screen)

	def draw(self, screen):
		drawer.drawImage(self.img, screen, (0,0))
		screenPosition = self.player.getScreenPosition()
		self.player.drawCharacter(screen, screenPosition)

		for v in self.victims:
			v.drawCharacter(screen, v.getScreenPosition())



	def movePlayer(self, deltaP):
		self.player.move(deltaP)

	def update(self):
		for v in self.victims:
			v.walk()
			v.seesPlayer(self.player)