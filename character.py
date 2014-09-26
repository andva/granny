class Character:
	def __init__(self):
		print "hej"

	def getBody(self):
		return self.physicsBody

	def debugDraw(self, screen):
		print "hej"
		#self.physicsBody.fixture.shape.draw(self.physicsBody, self.physicsBody.fixture, screen)