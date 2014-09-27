import pygame, sys
from pygame.locals import *

def drawAnim(image, anim, screen, screenPosition):
	img = pygame.image.load(image)
	anim.blit(screen, (screenPosition[0] - img.get_rect().size[0] / 2,screenPosition[1] - img.get_rect().size[1] + img.get_rect().size[1] / 4))


def drawImage(image, screen, screenPosition):
	screen.blit(image,(screenPosition[0], screenPosition[1]))