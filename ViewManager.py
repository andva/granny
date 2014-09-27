from level import Level
from player import Player

levels = []
cutscenes = []
currentView = [0]

def loadLevel(n, world):
	currentView[0] = levels[n]
	levels[n].initPhysics(world)

def loadCutscene(n):
	currentView[0] = cutscenes[n]

