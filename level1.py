from level import Level
from player import Player
from wall import Wall
from victim import Victim
from tasklist import TaskList
from tasklist import Task
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

		playerAnim = pyganim.PygAnimation([('images/granny.png', 0.1), ('images/granny2.png', 0.1), ('images/granny3.png', 0.1), ('images/granny2.png', 0.1), ('images/granny.png', 0.1), ('images/grannyr.png', 0.1), ('images/granny2r.png', 0.1), ('images/granny3r.png', 0.1), ('images/granny2r.png', 0.1), ('images/grannyr.png', 0.1)])
		self.player = Player((midx - 430 ,midy + 200), 'images/granny.png', playerAnim, world)
		self.walls = [
			#screenPos, Size
			# MAIN WALLS #############################################
			Wall((midx - 545, midy - 20), (3,250), world), #LEFT WALL
			Wall((midx, midy - 260), (540,3), world), # TOP WALL
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
			Wall((midx + 50, midy - 8), (470,3), world), # BOTTOM WALL

			]
		victimAnim = pyganim.PygAnimation([('images/granny.png', 0.1), ('images/granny2.png', 0.1), ('images/granny3.png', 0.1), ('images/granny2.png', 0.1), ('images/grannyr.png', 0.1), ('images/granny2r.png', 0.1), ('images/granny3r.png', 0.1), ('images/granny2r.png', 0.1)])
		self.victims = [
			Victim(
				(midx + 100, midy - 60),
				'images/granny.png',
				victimAnim,
				world,
				TaskList(
					#screenpos, time(ms), name
					[Task((201, 532), 6000, "a"),
					Task((207, 175), 6000, "b")]
				))
		]
		Level(self.player)
