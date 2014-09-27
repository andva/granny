import pygame, sys
from pygame.locals import *
import math
import Box2D

import constants
import debugRenderer
import pyganim
from level1 import Level1
from level2 import Level2
from cutscene import Cutscene
from soundManager import SoundManager
from musicManager import MusicManager
import listeners
import viewManager
from highscore import HighScore

def handleInput(highScore, sound):
	move = Box2D.b2Vec2(0,0)
	scale = constants.PLAYER_SPEED_REGULAR

	keys_pressed = pygame.key.get_pressed()
	if viewManager.currentView[0].type == 'level':
		if viewManager.currentView[0].player.anim.currentFrameNum < 11 and viewManager.currentView[0].player.left == True or viewManager.currentView[0].player.anim.currentFrameNum < 17 and viewManager.currentView[0].player.left == False:
			if keys_pressed[K_a]:
				move += (-1, 0)
			if keys_pressed[K_d]:
				move += (1, 0)
			if keys_pressed[K_w]:
				move += (0, 1)
			if keys_pressed[K_s]:
				move += (0, -1)
			if keys_pressed[K_RETURN]:
				sound.playCane()
				for v in viewManager.currentView[0].victims:
					playerX = viewManager.currentView[0].player.getScreenPosition()[0]
					playerY = viewManager.currentView[0].player.getScreenPosition()[1]
					victimX = v.getScreenPosition()[0]
					victimY = v.getScreenPosition()[1]
					if(math.hypot(playerX - victimX, playerY - victimY) < 60):
						v.dead = True
						if not v.seenPlayer:
							constants.highScore += 1000
							highScore.addScore(1000, (playerX,playerY))

						else:
							constants.highScore += 100
							highScore.addScore(100, (playerX,playerY))

				for d in viewManager.currentView[0].destructables:
					if (d.hitDelay()):
						playerX = viewManager.currentView[0].player.getScreenPosition()[0]
						playerY = viewManager.currentView[0].player.getScreenPosition()[1]
						victimX = d.getScreenPosition()[0]
						victimY = d.getScreenPosition()[1]
						if(math.hypot(playerX - victimX, playerY - victimY) < 90):
							sound.playBreaking()
							score = d.hit()
							if score > 0:
								highScore.addScore(score, (playerX,playerY))
							constants.highScore += d.hit()
					pass


	for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()

			if e.type == pygame.KEYDOWN:
				if e.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

				if e.key == pygame.K_b:
					constants.DEBUG = not constants.DEBUG

	move.Normalize()
	return move * scale

def resetForces(w):
	for body in w.bodies:
		body.__SetLinearVelocity((0,0))
		body.__SetAngularVelocity(0)

def initPygame():
	#pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.FULLSCREEN)
	pygame.display.set_caption("")
	constants.myfont = pygame.font.SysFont("trebuchet ms", 30)

	return screen

def initWorld():
	w = Box2D.b2World(gravity=(0,0),
					contactListener=listeners.ContactListener(),
					doSleep=True)

	Box2D.b2.circleShape.draw = debugRenderer.my_draw_circle
	Box2D.b2.polygonShape.draw = debugRenderer.my_draw_polygon

	return w

def render(w, screen):
	if (constants.DEBUG):
		for body in w.bodies:
			for fixture in body.fixtures:
				fixture.shape.draw(body, fixture, screen)
		viewManager.currentView[0].debugDraw(screen)

def worldAfterUpdate(w):
	w.Step(constants.TIME_STEP, constants.VEL_ITER, constants.POS_ITER)
	w.ClearForces()
	resetForces(w)
	if(viewManager.currentView[0].type == 'level'):
		i = 0
		for v in viewManager.currentView[0].victims:
			if(v.dead == True):
				x = v.getScreenPosition()[0]
				y = v.getScreenPosition()[1]
				viewManager.currentView[0].deadBodies.append((x,y))
				w.DestroyBody(v.physicsBody)
				del viewManager.currentView[0].victims[i]
			i += 1
		if len(viewManager.currentView[0].victims) == 0:
			for v in w.bodies:
				w.DestroyBody(v)

			if (viewManager.currentLevel[0] == 0):
				viewManager.loadLevel(1, w)
				viewManager.currentView[0].deadBodies = []
			if (viewManager.currentLevel[0] == 1):
				viewManager.loadLevel(1, w)

def main():
	screen = initPygame()
	w = initWorld()
	highscoore = HighScore()
	level1 = Level1(w, 'images/level1.png', 0)
	cutscene1 = Cutscene('images/cutscene.png',0)
	level2 = Level2(w, 'images/level2.png', 1)

	sound = SoundManager()
	music = MusicManager()

	viewManager.levels.insert(0, level1)
	viewManager.cutscenes.insert(0, cutscene1)
	viewManager.levels.insert(1, level2)
	clock = pygame.time.Clock()
	viewManager.loadCutscene(0)
	playtime = 0
	while True:
		screen.fill((100,100,100,0))
		milliseconds = clock.tick(constants.FPS)
		playtime += milliseconds / 1000.0

		move = handleInput(highscoore, sound)

		viewManager.currentView[0].draw(screen)

		for h in highscoore.entries:
			label = constants.myfont.render(str(h.score), 1, (255,0,0))
			pos = h.screenPos
			screen.blit(label, (pos[0] - 70, pos[1] - 100))

		viewManager.currentView[0].movePlayer(move)
		viewManager.currentView[0].update(w)
		if viewManager.currentView[0].type == 'level':
			if len(viewManager.currentView[0].victims) == 0:
				pass


		render(w, screen)
		highscoore.update()
		worldAfterUpdate(w)
		text = "FPS: {0:.2f}   Playtime: {1:.2f} ".format(clock.get_fps(), playtime) + "Score: " + str(highscoore.totalScore)
		pygame.display.set_caption(text)
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()