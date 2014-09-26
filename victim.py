import character
import constants

class Victim(character.Character):
	def __init__(self, screenPosition, world):
		self.screenPosition = screenPosition
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(screenPosition), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)

	def draw(self):
		print "hej"