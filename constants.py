import Box2D

PPM=20.0
SCREEN_WIDTH, SCREEN_HEIGHT=1280,720

DEBUG_COLORS = {
	Box2D.b2.staticBody  : (255,100,0,255),
	Box2D.b2.dynamicBody : (127,60,227,255),
}

TIME_STEP = 1.0 / 60.
VEL_ITER, POS_ITER = 6, 2

DEBUG = False

def screen2WorldNoFlip(pos):
	return [p / PPM for p in pos]

def screen2World(pos):
	if (len(pos) > 1):
		position = [pos[0], SCREEN_HEIGHT - pos[1]]
	return screen2WorldNoFlip(position)

def world2ScreenNoFlip(pos):
	return [p * PPM for p in pos]

def world2Screen(pos):
	position = world2ScreenNoFlip(pos)
	if (len(position) > 1):
		position = [position[0], SCREEN_HEIGHT - position[1]]
	return position