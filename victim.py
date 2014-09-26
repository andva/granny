import character

class Victim(character.Character):
	def __init__(self, position):
		self.position = position

	def draw(self):
		print "hej"