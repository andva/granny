import character

class Player(character.Character):
	def __init__(self, position, world):
		self.position = position
		self.physicsBody = world.CreateDynamicBody(position=(10,15), angle=15)
		self.physicsBody.CreateCircleFixture(radius=1.0, friction=0.0, density=0.3)

	def move(self, deltaP):
		self.physicsBody.ApplyLinearImpulse(deltaP, self.physicsBody.position, True)