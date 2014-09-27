import Box2D
import constants
class Wall:
	def __init__(self, screenPos, size, w):
		self.screenPos = screenPos
		self.size = size

	def addPhysics(self, world):
		worldSize = constants.screen2WorldNoFlip(self.size)
		worldPos = constants.screen2World(self.screenPos)
		self.body = world.CreateStaticBody(
			position = worldPos,
			shapes = Box2D.b2.polygonShape(box=worldSize),
			)