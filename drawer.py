import pygame, sys
from pygame.locals import *

def drawImage(image, screen, screenPosition):
	img = pygame.image.load(image)
	screen.blit(img,(screenPosition[0],screenPosition[1]))
