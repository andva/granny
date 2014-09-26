import character
import constants
import Box2D

class Victim(character.Character):
	def __init__(self, screenPosition, image, world):
		self.screenPosition = screenPosition
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(screenPosition), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
		self.image = image
		self.direction = (1, 0)
		verts = [Box2D.b2Vec2(0,0), Box2D.b2Vec2(-5,5), Box2D.b2Vec2(5,5)]
		count = 3
		shape = Box2D.b2PolygonShape()
		self.fovBody = world.CreateStaticBody(
			position=constants.screen2World(screenPosition),
			angle=0,
			shapes = Box2D.b2.polygonShape(vertices=verts, vertexCount=count),
			#shapeFixture = Box2D.b2.b2FixtureDef(sensor=False)
			)
	def draw(self):
		print "hej"