from level import Level
from player import Player
from wall import Wall
from victim import Victim
from tasklist import TaskList
from tasklist import Task
from destructable import Destructable
from room import Room
import constants
import pyganim
import pygame, sys
from pygame.locals import *

class Level1(Level):
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
		self.player = Player((midx - 430 ,midy + 200), 'images/granny.png', playerAnim, world)
		Level.__init__(self, self.player)
		self.walls = [
			#screenPos, Size
			# MAIN WALLS #############################################
			Wall((midx - 545, midy - 20), (3,250), world), #LEFT WALL
			Wall((midx - 235, midy - 205), (345,70), world), # TOP WALL
			Wall((midx + 350, midy - 305), (240,50), world), # TOP WALL

			Wall((midx, midy + 220), (540,3), world), # BOTTOM WALL
			Wall((midx + 522, midy - 155), (3,90), world), #RIGHT WALL TOP
			Wall((midx + 522, midy + 120), (3,110), world), #RIGHT WALL BOTTOM
			Wall((midx + 600, midy + 20), (60,3), world), #OUTSIDE TOP
			Wall((midx + 600, midy - 65), (60,3), world), #OUTSIDE BOTTOM

			# GRANNY ROOM ############################################
			Wall((midx - 386, midy + 110), (10,120), world), #GRANNY RIGHT WALL LARGE
			Wall((midx - 410, midy + 15), (10,30), world), #GRANNY RIGHT WALL SMALL
			Wall((midx - 510, midy + 60 ), (40,70), world), #GRANNY LEFT WALL

			# CORRIDOR ##############################################
			Wall((midx - 60, midy + 100), (300,120), world), # BOTTOM WALL
			Wall((midx - 60, midy + 160), (350,100), world), # BOTTOM WALL 2
			Wall((midx + 410, midy + 160), (25, 300), world), # RECEPTION WALL
			Wall((midx + 300, midy - 120), (100, 30), world), # RECEPTION WALL
			Wall((midx + 390, midy + 90), (40, 30), world), # RECEPTION WALL

			]

		self.rooms = [
			Room(0, (midx - 500, midy + 180), (300, 300)),
			Room(1, (midx - 155, midy - 60), (750, 170)),
			Room(2, (midx + 320, midy - 222), (440, 150)),
			Room(3, (midx + 320, midy + 70), (200, 400)),
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

					Task((964, 386), 3000, "a"),
					Task((374, 291), 3000, "b"),
					#Task((1215, 342), 2000, "c"),
					]
				)),

		]
		tvAnim = pyganim.PygAnimation([('images/tv.png', 0.1), ('images/tv3.png', 0.1), ('images/tv4.png', 0.1)])
		self.destructables = [
			Destructable((midx + 430, 500), tvAnim, 'images/tv.png'),
			Destructable((midx + 250, 510), tvAnim, 'images/tv.png'),
		]

		self.asignRooms()

		#Level(self.player)
