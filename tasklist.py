import random
import pygame

class Task:
	def __init__(self, screenPos, time, name):
		self.screenPos = screenPos
		self.time = time
		self.name = name

class TaskList:
	def __init__(self, tasks):
		self.tasks = tasks
		self.currentTaskId = -1
		self.currentTaskId = self.getRandomTask()
		self.startTime = 0
		self.done = True

	def addTask(self, task):
		self.tasks.append(task)

	def getRandomTask(self):

		r = random.randint(0, len(self.tasks) - 2)
		if (r >= self.currentTaskId): r += 1
		print "TASKLIST", r
		self.currentTaskId = r
		return self.tasks[r]

	def startDoingTask(self):
		self.startTime = pygame.time.get_ticks()
		self.done = False

	def done(self):
		return self.done

	def update(self):
		timeWorked = pygame.time.get_ticks() - self.startTime
		self.done = (timeWorked >= self.tasks[self.currentTaskId].time)