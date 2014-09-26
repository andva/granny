import Box2D

class ContactListener(Box2D.b2ContactListener):
    def __init__(self):
        Box2D.b2ContactListener.__init__(self)
    def BeginContact(self, contact):
        print "hej"
    def EndContact(self, contact):
        pass
    def PreSolve(self, contact, oldManifold):
        pass
    def PostSolve(self, contact, impulse):
		pass

class MyContactFilter(Box2D.b2ContactFilter):
    def __init__(self):
        Box2D.b2ContactFilter.__init__(self)
    def ShouldCollide(self, shape1, shape2):
        # Implements the default behavior of b2ContactFilter in Python
        print "sc"
        filter1 = shape1.filterData
        filter2 = shape2.filterData
        if filter1.groupIndex == filter2.groupIndex and filter1.groupIndex != 0:
            return filter1.groupIndex > 0

        collides = (filter1.maskBits & filter2.categoryBits) != 0 and (filter1.categoryBits & filter2.maskBits) != 0
        return collides