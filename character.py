import pygame, sys
from pygame.locals import *
import Box2D

class Character:
	def __init__(self):
		print "hej"

	def getBody(self):
		return self.physicsBody