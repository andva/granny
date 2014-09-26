import character
import constants

class Player(character.Character):
	def __init__(self, screenPosition, world):
		self.screenPosition = screenPosition
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(screenPosition), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)

	def move(self, deltaP):
		self.physicsBody.ApplyLinearImpulse(deltaP, self.physicsBody.position, True)

	def draw(self, screen):
		print "hej"