class Task:
	def __init__(self, screenPos, time):
		self.screenPos = screenPos
		self.time = time

class TaskList:
	def __init__(self):
		self.tasks = []

	def addTask(self, task):
		self.tasks.append(task)
