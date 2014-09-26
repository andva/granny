import pygame, sys
from pygame.locals import *
import Box2D

from soundManager import SoundManager

import debugRenderer

def main():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.init()

	screen = pygame.display.set_mode((640, 480))

	pygame.display.set_caption("Hello World")

	w = Box2D.b2World(gravity=(0,0), doSleep=True)

	groundBody = w.CreateStaticBody(
		position=(0,-3),
		shapes = Box2D.b2.polygonShape(box=(50,5)),
		)
	Box2D.b2.circleShape.draw = debugRenderer.my_draw_circle
	Box2D.b2.polygonShape.draw = debugRenderer.my_draw_polygon
	dynamic_body = w.CreateDynamicBody(position=(10,15), angle=15)

	dynamic_body.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)
	timeStep = 1.0 / 60.
	velIter, posIter = 6, 2

	sound = SoundManager()

	while True:
		screen.fill((0,0,0,0))

		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()

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

		dynamic_body.ApplyLinearImpulse(move * scale, dynamic_body.position, True)

		for body in w.bodies:
			for fixture in body.fixtures:
				fixture.shape.draw(body, fixture, screen)

		w.Step(timeStep, velIter, posIter)

		w.ClearForces()
		dynamic_body.__SetLinearVelocity((0,0))
		dynamic_body.__SetAngularVelocity(0)
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()