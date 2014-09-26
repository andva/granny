import pygame, sys
from pygame.locals import *

def drawImage(image,screen):
	img = pygame.image.load(image)
	screen.blit(img,(0,0))
