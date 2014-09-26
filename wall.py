import Box2D
import constants
class Wall:
	def __init__(self, screenPos, size, w):
		worldSize = constants.screen2World(size)
		worldPos = constants.screen2World(screenPos)
		print worldPos, worldSize
		self.body = w.CreateStaticBody(
			position = worldPos,
			shapes = Box2D.b2.polygonShape(box=worldSize),
			)