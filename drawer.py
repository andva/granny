import pygame, sys
from pygame.locals import *

def drawImage(image, screen, screenPosition):
	img = pygame.image.load(image)
	screen.blit(img,(screenPosition[0] - img.get_rect().size[0] / 2,screenPosition[1] - img.get_rect().size[1] + img.get_rect().size[1] / 4))
