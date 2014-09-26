import Box2D

PPM=20.0
SCREEN_WIDTH, SCREEN_HEIGHT=640,480

DEBUG_COLORS = {
	Box2D.b2.staticBody  : (255,100,0,255),
	Box2D.b2.dynamicBody : (127,60,227,255),
}

TIME_STEP = 1.0 / 60.
VEL_ITER, POS_ITER = 6, 2

DEBUG = True

def screen2World(pos):
	if (len(pos) > 1):
		position = [pos[0], SCREEN_HEIGHT - pos[1]]
	return [p / PPM for p in position]

def world2Screen(pos):
	position = [p * PPM for p in pos]
	if (len(position) > 1):
		position = [position[0], SCREEN_HEIGHT - position[1]]
	return position