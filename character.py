import drawer

class Character:

	image = 0

	def __init__(self):
		pass

	def getBody(self):
		return self.physicsBody

	def debugDraw(self, screen):
		print "hej"
		#self.physicsBody.fixture.shape.draw(self.physicsBody, self.physicsBody.fixture, screen)

	def drawCharacter(self, screen, screenPosition):
		drawer.drawImage(self.image, screen, screenPosition)