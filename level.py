import drawer
import pygame, sys
from pygame.locals import *

class Level(object):

	id = 0
	image = 0
	img = 0
	type = 'level'
	deadBodies = []

	def __init__(self, player):
		print "hej"
		self.player = player
		self.victims = []
		self.destructables = []
		self.bodies = []
		self.walls = []
		self.rooms = []


	def debugDraw(self, screen):
		self.player.debugDraw(screen)
		for r in self.rooms:
			#r.debugDraw(screen)
			pass
	def draw(self, screen):
		drawer.drawImage(self.img, screen, (0,0))
		screenPosition = self.player.getScreenPosition()
		for bodyPos in self.deadBodies:
			img = pygame.image.load('images/deadbody.png')
			drawer.drawImage(img, screen, (bodyPos[0] - img.get_rect().size[0] / 2, bodyPos[1] - img.get_rect().size[0] / 2))
		self.player.drawCharacter(screen, screenPosition)
		for v in self.victims:
			v.drawCharacter(screen, v.getScreenPosition())
		for d in self.destructables:
			d.drawDestructable(screen)


	def movePlayer(self, deltaP):
		self.player.move(deltaP)

	def update(self, world):
		self.asignRooms()
		for v in self.victims:
			v.testIfSeesPlayer(self.player, world)
			v.walk()

	def asignRooms(self):
		#for v in self.victims:
		sp = self.player.getScreenPosition()
		for r in self.rooms:
			rsp = r.screenPos
			rsx = r.screenSize[0] / 2.
			rsy = r.screenSize[1] / 2.

			if rsp[0] - rsx < sp[0] <= rsp[0] + rsx and rsp[1] - rsy < sp[1] <= rsp[1] + rsy:
				self.player.currentRoom = r.id
		for v in self.victims:
			sp = v.getScreenPosition()
			for r in self.rooms:
				rsp = r.screenPos
				rsx = r.screenSize[0] / 2.
				rsy = r.screenSize[1] / 2.

				if rsp[0] - rsx < sp[0] <= rsp[0] + rsx and rsp[1] - rsy < sp[1] <= rsp[1] + rsy:
					v.currentRoom = r.id

	def initPhysics(self, world):
		self.player.addPhysics(world)
		for v in self.victims:
			v.addPhysics(world)
		for w in self.walls:
			w.addPhysics(world)
