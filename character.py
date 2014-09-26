import constants
import drawer

class Character:
	def __init__(self):

	def getBody(self):
		return self.physicsBody

	def debugDraw(self, screen):
		print "hej"
		#self.physicsBody.fixture.shape.draw(self.physicsBody, self.physicsBody.fixture, screen)

	def drawCharacter(self, screen, screenPosition):
		drawer.drawImage('images/snakehead2.png', screen, screenPosition)

	def getScreenPosition(self):
		return constants.world2Screen(self.physicsBody.position)