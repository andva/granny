import character
import constants
import math
import Box2D
import pygame
import drawer
from astar import AStarGrid, AStarGridNode
from itertools import product

class Victim(character.Character):

	moving = False
	dead = False

	def __init__(self, screenPosition, image, anim, world):
		super(Victim, self).__init__()
		self.startPositionScreen = screenPosition
		self.anim = anim
		self.image = image
		self.fovAngle = 60
		self.direction = (1, 0)
		self.path = []
		graph, nodes = self.createCollisionMap()
		paths = AStarGrid(graph)
		self.setWaypoint((screenPosition[0], screenPosition[1] + 100), nodes, paths)

	def createCollisionMap(self):
		collisionMap = pygame.image.load("images/collisionMap.png").convert()
		rect = collisionMap.get_rect()
		width = rect[2]
		height = rect[3]
		nodes = [[AStarGridNode(x, y) for y in range(height)] for x in range(width)]
		graph = {}
		for x, y in product(range(rect[2]),range(rect[3])):
			node = nodes[x][y]
			graph[node] = []
			for i, j in product([-1, 0, 1], [-1, 0, 1]):
				if not (0 <= x + i < width): continue
				if not (0 <= y + j < height): continue
				pixelVal = collisionMap.get_at((x + i, y + j))[0]
				if pixelVal < 100: continue
				graph[nodes[x][y]].append(nodes[x+i][y+j])
		return graph, nodes

	def convertToPathCoord(self, x, y):
		return [int(x * constants.PATH_MAP_SCALE), int(y * constants.PATH_MAP_SCALE)]

	def setWaypoint(self, goal, nodes, paths):
		start = self.convertToPathCoord(self.startPositionScreen[0], self.startPositionScreen[1])
		goalI = self.convertToPathCoord(self.startPositionScreen[0] + 100, self.startPositionScreen[1])
		s, e = nodes[start[0]][start[1]], nodes[goalI[0]][goalI[1]]
		self.path = paths.search(s, e)
		if self.path is None:
			print "No path"
		else:
			print "Found path", constants.pathToScreen([self.path[0].x, self.path[0].y])
		print self.startPositionScreen[0], self.startPositionScreen[1], start, goalI

	def addPhysics(self, world):
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(self.startPositionScreen), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
		self.initialized = True

	def draw(self):
		pass

	def walk(self):
		if not self.initialized: return;
		d = ((pygame.time.get_ticks()%5000)/2500)
		if (d == 1):
			dir = (0,1)
			self.moving = False
		else:
			dir = (0,-1)
			self.moving = True

		self.direction = dir
		movement = [dir[0] * constants.VICTIM_SPEED_REGULAR * 0.8, dir[1] * constants.VICTIM_SPEED_REGULAR * 0.8]
		self.screenPosition = constants.world2Screen(self.physicsBody.position)

		self.physicsBody.ApplyLinearImpulse(movement, self.physicsBody.position, True)

	def calcFovPolygon(self):
		sp = self.getScreenPosition()
		rv1 = constants.rotateVector(self.direction, self.fovAngle / 2.)
		rv2 = constants.rotateVector(self.direction, -self.fovAngle / 2.)
		return [
			sp,
			(sp[0] - rv1[0] * 500., sp[1] - rv1[1] * 500.),
			(sp[0] - rv2[0] * 500., sp[1] - rv2[1] * 500.)
		]

	def drawCharacter(self, screen, screenPosition):
		if(self.dead == False):
			if(self.moving == True):
				self.anim.play()
			else:
				self.anim.pause()
				self.anim.currentFrameNum = 0
			drawer.drawAnim(self.image, self.anim, screen, screenPosition)
			#draw fov

			pygame.draw.polygon(screen, (80,80,100,10), self.calcFovPolygon())

	def seesPlayer(self, player):
		if not self.initialized: return
		playerScreenPos = player.getScreenPosition()
		victimToPlayer = Box2D.b2Vec2((playerScreenPos[0] - self.screenPosition[0],playerScreenPos[1] - self.screenPosition[1]));
		victimToPlayer.Normalize()
		rawDot = Box2D.b2Dot(victimToPlayer, (-self.direction[0], -self.direction[1]))
		if (rawDot > 0):
			dot = constants.rad2deg(math.acos(rawDot))
			if (dot < self.fovAngle / 2.):
				pass
