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
		self.walls = []


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

	def update(self, world):
		for v in self.victims:
			v.walk()
			v.seesPlayer(self.player)

	def initPhysics(self, world):
		self.player.addPhysics(world)
		for v in self.victims:
			v.addPhysics(world)
		for w in self.walls:
			w.addPhysics(world)
