import constants
import pyganim


class Character:

	anim = pyganim.PygAnimation([('images/granny.png', 0.2), ('images/granny.png', 0.2)])
	image = 0

	def __init__(self):
		pass

	def getBody(self):
		return self.physicsBody

	def debugDraw(self, screen):
		print "hej"
		#self.physicsBody.fixture.shape.draw(self.physicsBody, self.physicsBody.fixture, screen)

	def getScreenPosition(self):
		return constants.world2Screen(self.physicsBody.position)
