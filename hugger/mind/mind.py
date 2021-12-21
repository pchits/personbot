
from sphere import Sphere
import constants

class Mind:

    def __init__(self, world, mind, socium):
        #  init spheres
        self.sphereWorld = Sphere(constants.TIMER_START, constants.ENERGY_MAX, world)
        self.sphereMind = Sphere(constants.TIMER_START, constants.ENERGY_MAX, mind)
        self.sphereSocium = Sphere(constants.TIMER_START, constants.ENERGY_MAX, socium)







