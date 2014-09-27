import constants
import pyganim


class Character(object):

	anim = []
	image = 0

	def __init__(self):
		self.initialized = False;
		pass

	def getBody(self):
		if (self.initialized):
			return self.physicsBody
		return 0

	def debugDraw(self, screen):
		print "hej"
		#self.physicsBody.fixture.shape.draw(self.physicsBody, self.physicsBody.fixture, screen)

	def getScreenPosition(self):
		if (self.initialized):
			return constants.world2Screen(self.physicsBody.position)
		return (0,0)