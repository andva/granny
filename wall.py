import Box2D
import constants
class Wall:
	def __init__(self, screenPos, size, w):
		worldSize = constants.screen2WorldNoFlip(size)
		worldPos = constants.screen2World(screenPos)
		print "Wall", screenPos, size, worldSize, worldPos
		self.body = w.CreateStaticBody(
			position = worldPos,
			shapes = Box2D.b2.polygonShape(box=worldSize),
			)