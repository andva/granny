import Box2D

class Wall:
	def __init__(self, pos, size, w):
		groundBody = w.CreateStaticBody(
			position=pos,
			shapes = Box2D.b2.polygonShape(box=size),
			)