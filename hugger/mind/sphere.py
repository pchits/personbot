

class Sphere:

    def __init__(self, type, lifetime, energy, feature, input = 0, world = 0):
        # set sphere type
        self.type = type
        # set sphere's characteristics
        self.lifetime = lifetime
        self.energy = energy
        self.feature = feature
        # set sphere's external connections
        self.input = input
        self.world = world


    def save(self):
        # saving sphere
        print('test')
