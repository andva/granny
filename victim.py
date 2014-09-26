import character
import constants
import math
import Box2D
import pygame
import drawer

class Victim(character.Character):
	def __init__(self, screenPosition, image, anim, world):
		self.screenPosition = screenPosition
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(screenPosition), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
		self.anim = anim
		self.image = image
		self.fovAngle = 60
		self.direction = (1, 0)
		# verts = [Box2D.b2Vec2(0,0), Box2D.b2Vec2(-5,5), Box2D.b2Vec2(5,5)]
		# count = 3
		# shape = Box2D.b2PolygonShape()
		# self.fovBody = world.CreateStaticBody(
		# 	position=constants.screen2World(screenPosition),
		# 	angle=0,
		# 	shapes = Box2D.b2.polygonShape(vertices=verts, vertexCount=count),
		# 	)
	def draw(self):
		print "hej"

	def walk(self):
		if True: return
		d = ((pygame.time.get_ticks()%5000)/2500)
		if (d == 1):
			self.direction = (0,1)
		else:
			self.direction = (0,-1)
		self.screenPosition = constants.world2Screen(self.physicsBody.position)
		self.physicsBody.ApplyLinearImpulse(self.direction, self.physicsBody.position, True)

	def draw(self):
		print "hej"

	def drawCharacter(self, screen, screenPosition):
		self.anim.pause()
		drawer.drawImage(self.image, self.anim, screen, screenPosition)
		#draw fov
		sp = self.getScreenPosition()
		rv1 = constants.rotateVector(self.direction, self.fovAngle / 2.)
		rv2 = constants.rotateVector(self.direction, -self.fovAngle / 2.)
		v = [
			sp,
			(sp[0] - rv1[0] * 500., sp[1] - rv1[1] * 500.),
			(sp[0] - rv2[0] * 500., sp[1] - rv2[1] * 500.)
		]
		pygame.draw.polygon(screen, (80,80,100,255), v)

	def seesPlayer(self, player):
		playerScreenPos = player.getScreenPosition()

		victimToPlayer = Box2D.b2Vec2((playerScreenPos[0] - self.screenPosition[0],playerScreenPos[1] - self.screenPosition[1]));
		victimToPlayer.Normalize()
		rawDot = Box2D.b2Dot(victimToPlayer, (-self.direction[0], -self.direction[1]))
		if (rawDot > 0):
			dot = constants.rad2deg(math.acos(rawDot))
			if (dot < self.fovAngle / 2.):
				print "I SEE YOU", dot