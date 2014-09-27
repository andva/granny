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

	def __init__(self, screenPosition, image, anim, world, taskList):
		super(Victim, self).__init__()
		self.startPositionScreen = screenPosition
		self.screenPosition = screenPosition
		self.anim = anim
		self.image = image
		self.fovAngle = 60
		self.direction = (1, 0)
		self.path = []
		self.taskList = taskList
		self.graph, self.nodes = self.createCollisionMap()
		self.paths = AStarGrid(self.graph)

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
				if not (0 <= x + i < width - 1): continue
				if not (0 <= y + j < height - 1): continue
				pixelVal = collisionMap.get_at((x + i, y + j))[0]
				if pixelVal < 10: continue
				graph[nodes[x][y]].append(nodes[x+i][y+j])
		return graph, nodes

	def convertToPathCoord(self, x, y):
		return [int(x * constants.PATH_MAP_SCALE), int(y * constants.PATH_MAP_SCALE)]

	def convertPathToScreenCoord(self, x, y):
		return [float(x) * constants.PATH_MAP_INV_SCALE, float(y) * constants.PATH_MAP_INV_SCALE]

	def setWaypoint(self, goal):
		start = self.convertToPathCoord(self.screenPosition[0], self.screenPosition[1])
		goalI = self.convertToPathCoord(goal[0], goal[1])

		self.graph, self.nodes = self.createCollisionMap()
		self.paths = AStarGrid(self.graph)

		s, e = self.nodes[start[0]][start[1]], self.nodes[goalI[0]][goalI[1]]
		self.path = self.paths.search(s, e)
		if len(self.path) == 0:
			print "No path"
		else:
			print "Found path", self.convertPathToScreenCoord(self.path[0].x, self.path[0].y), len(self.path)

	def addPhysics(self, world):
		self.physicsBody = world.CreateDynamicBody(position=constants.screen2World(self.startPositionScreen), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
		self.initialized = True

	def draw(self):
		pass

	def walk(self):
		self.screenPosition = constants.world2Screen(self.physicsBody.position)
		if (len(self.path) > 0):
			targetPos = self.convertPathToScreenCoord(self.path[0].x, self.path[0].y)
			xd = targetPos[0] - self.screenPosition[0]
			yd = targetPos[1] - self.screenPosition[1]
			if (abs(xd) <= 7.1 and abs(yd) <= 7.1):
				self.path.pop(0)

			self.direction = Box2D.b2Vec2([
				(targetPos[0] - self.screenPosition[0]),
				-(targetPos[1] - self.screenPosition[1])])
			self.direction.Normalize()
			movement = [self.direction[0] * constants.VICTIM_SPEED_REGULAR * 0.8, self.direction[1] * constants.VICTIM_SPEED_REGULAR * 0.8]
			self.physicsBody.ApplyLinearImpulse(movement, self.physicsBody.position, True)
		elif self.taskList.done:
			goal = self.taskList.getRandomTask().screenPos
			print "Setting new task"
			self.setWaypoint(goal)
			print "done"

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
			ptlst = []
			if (self.path != None):
				if (len(self.path) > 1):
					for i in range(0, len(self.path) - 1):
						start = self.convertPathToScreenCoord(self.path[i].x, self.path[i].y)
						end = self.convertPathToScreenCoord(self.path[i + 1].x, self.path[i + 1].y)
						pygame.draw.line(screen, (255, 0, 0, 0), start, end, 10)

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
