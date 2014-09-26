import pygame, sys
from pygame.locals import *
import Box2D

import constants
import debugRenderer
import player
from player import Player

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

def resetForces(player):
	body = player.getBody()
	body.__SetLinearVelocity((0,0))
	body.__SetAngularVelocity(0)

def initPygame():
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Hello World")
	return screen

def main():
	pygame.init()

	screen = initPygame()
	w = Box2D.b2World(gravity=(0,0), doSleep=True)
	Box2D.b2.circleShape.draw = debugRenderer.my_draw_circle
	Box2D.b2.polygonShape.draw = debugRenderer.my_draw_polygon
	player = Player((10,15), w)
	groundBody = w.CreateStaticBody(
		position=(0,-3),
		shapes = Box2D.b2.polygonShape(box=(50,5)),
		)

	while True:
		screen.fill((0,0,0,0))

		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()

		move = handleInput()

		player.move(move)

		for body in w.bodies:
			for fixture in body.fixtures:
				fixture.shape.draw(body, fixture, screen)

		w.Step(constants.TIME_STEP, constants.VEL_ITER, constants.POS_ITER)

		w.ClearForces()
		resetForces(player)
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()