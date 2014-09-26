import pygame, sys
from pygame.locals import *
import Box2D

import constants
import debugRenderer
from level1 import Level1
from soundManager import SoundManager
from musicManager import MusicManager
from character import Character

def handleInput():
	move = Box2D.b2Vec2(0,0)
	scale = 2.0

	keys_pressed = pygame.key.get_pressed()
	if keys_pressed[K_a]:
		move += (-1, 0)
	if keys_pressed[K_d]:
		move += (1, 0)
	if keys_pressed[K_w]:
		move += (0, 1)
	if keys_pressed[K_s]:
		move += (0, -1)
	move.Normalize()
	return move * scale

def resetForces(w):
	for body in w.bodies:
		body.__SetLinearVelocity((0,0))
		body.__SetAngularVelocity(0)

def initPygame():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	pygame.display.set_caption("Hello World")
	return screen

def initWorld():
	w = Box2D.b2World(gravity=(0,0), doSleep=True)
	Box2D.b2.circleShape.draw = debugRenderer.my_draw_circle
	Box2D.b2.polygonShape.draw = debugRenderer.my_draw_polygon
	return w

def render(w, screen):
	if (constants.DEBUG):
		for body in w.bodies:
			for fixture in body.fixtures:
				fixture.shape.draw(body, fixture, screen)

def worldAfterUpdate(w):
	w.Step(constants.TIME_STEP, constants.VEL_ITER, constants.POS_ITER)
	w.ClearForces()
	resetForces(w)

def main():
	screen = initPygame()
	w = initWorld()

	level1 = Level1(w)

	sound = SoundManager()
	music = MusicManager()


	while True:
		screen.fill((100,100,100,0))

		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()

		move = handleInput()

		level1.draw(screen)
		level1.movePlayer(move)

		render(w, screen)

		worldAfterUpdate(w)

		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()