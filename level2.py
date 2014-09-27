from level import Level
from player import Player
from wall import Wall
from victim import Victim
from tasklist import TaskList
from tasklist import Task
from room import Room
import constants
import pyganim
import pygame, sys
from destructable import Destructable
from pygame.locals import *

class Level2(Level):
	def __init__(self, world, image, id):
		midx = constants.SCREEN_WIDTH / 2.0
		midy = constants.SCREEN_HEIGHT / 2.0
		self.id = id
		self.image = image
		self.img = pygame.image.load(image).convert()

		playerAnim = pyganim.PygAnimation([('images/granny.png', 0.1), ('images/granny2.png', 0.1), ('images/granny3.png', 0.1), ('images/granny2.png', 0.1), ('images/granny.png', 0.1),
										   ('images/grannyr.png', 0.1), ('images/granny2r.png', 0.1), ('images/granny3r.png', 0.1), ('images/granny2r.png', 0.1), ('images/grannyr.png', 0.1),
										   ('images/grannyf.png', 0.1), ('images/grannyf2.png', 0.1), ('images/grannyf3.png', 0.1), ('images/grannyf2.png', 0.1), ('images/grannyf.png', 0.1), ('images/granny.png', 0.1),
										   ('images/grannyfr.png', 0.1), ('images/grannyf2r.png', 0.1), ('images/grannyf3r.png', 0.1), ('images/grannyf2r.png', 0.1), ('images/grannyfr.png', 0.1), ('images/granny.png', 0.1)])
		self.player = Player((midx - 0 ,midy + 300), 'images/granny.png', playerAnim, world)
		Level.__init__(self, self.player)
		self.walls = [
			#screenPos, Size
			# MAIN WALLS #############################################
			Wall((midx - 635, midy - 90), (3,300), world),
			Wall((midx + 620, midy - 90), (3,300), world),
			Wall((midx + 640, midy - 310), (1280,3), world),
			Wall((midx + 440, midy + 175), (400,40), world),
			Wall((midx - 450, midy + 175), (400,40), world),
			Wall((midx - 465, midy - 130), (380,30), world),
			Wall((midx + 270, midy - 130), (225,30), world),
			Wall((midx - 450, midy + 67), (15,100), world),
			Wall((midx - 470, midy + 10), (30,40), world),
			Wall((midx - 240, midy + 120), (15,40), world),
			Wall((midx - 240, midy - 50), (15,40), world),
			Wall((midx + 210, midy + 60), (15,70), world),
			Wall((midx + 123, midy - 170), (15,20), world),
			Wall((midx + 430, midy - 170), (15,20), world),
			Wall((midx - 155, midy - 200), (10,40), world),
			Wall((midx + 440, midy + 350), (400,40), world),
			Wall((midx - 450, midy + 350), (400,40), world),
			]

		self.rooms = [
			Room(0, (midx - 20, midy + 30), (450, 320)),
			Room(1, (midx + 430, midy + 30), (450, 320)),
			Room(2, (midx - 350, midy + 30), (220, 320)),
			Room(3, (midx - 570, midy + 30), (220, 320)),
			Room(4, (midx + 360, midy - 290), (500, 320)),
			Room(5, (midx - 20, midy - 290), (250, 310)),
			Room(6, (midx - 400, midy - 290), (500, 310)),

		]

		victimAnim = pyganim.PygAnimation([('images/victim.png', 0.1), ('images/victim2.png', 0.1), ('images/victim3.png', 0.1), ('images/victim2.png', 0.1), ('images/victim.png', 0.1),
										   ('images/victimr.png', 0.1), ('images/victim2r.png', 0.1), ('images/victim3r.png', 0.1), ('images/victim2r.png', 0.1), ('images/victimr.png', 0.1)])
		self.victims = [
			Victim(
				(midx + 100, midy - 60),
				'images/victim.png',
				victimAnim,
				world,
				TaskList([
					#screenpos, time(ms), name
					Task((284, 138), 2000, "a"),
					Task((623, 391), 2000, "b"),
					Task((1151, 417), 2000, "c"),
					Task((290, 403), 2000, "c"),
					Task((1167, 129), 2000, "c"),
					]
				),
				'images/collisionMap2.png'
			),
			Victim(
				(midx + 500, midy - 100),
				'images/victim.png',
				victimAnim,
				world,
				TaskList([
					#screenpos, time(ms), name
					Task((284, 138), 2000, "a"),
					Task((623, 391), 2000, "b"),
					Task((1151, 417), 2000, "c"),
					Task((290, 403), 2000, "c"),
					Task((1167, 129), 2000, "c"),
					]
				),
				'images/collisionMap2.png'
			),
			Victim(
				(midx - 500, midy - 60),
				'images/victim.png',
				victimAnim,
				world,
				TaskList([
					#screenpos, time(ms), name
					Task((284, 138), 2000, "a"),
					Task((623, 391), 2000, "b"),
					Task((290, 403), 2000, "c"),
					Task((1167, 129), 2000, "c"),
					Task((1151, 417), 2000, "c"),
					]
				),
				'images/collisionMap2.png'
			),
		]

		tvAnim = pyganim.PygAnimation([('images/tv.png', 0.1), ('images/tv3.png', 0.1), ('images/tv4.png', 0.1)])
		self.destructables = [
			Destructable((13, 107), tvAnim, 'images/tv.png'),
			Destructable((13, 439), tvAnim, 'images/tv.png'),
		]



		self.asignRooms()

