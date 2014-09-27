from level import Level
from player import Player

levels = []
cutscenes = []
currentView = [0]
currentLevel = [-1]
def loadLevel(n, world):
	currentView[0] = levels[n]
	levels[n].initPhysics(world)
	currentLevel[0] = n
def loadCutscene(n):
	currentView[0] = cutscenes[n]

