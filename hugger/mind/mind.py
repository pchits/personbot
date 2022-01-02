
from hugger.constants import TIMER_FINISH
from sphere import Sphere
import random

import constants
from ..connector import CUR

class Mind:

    def __init__(self, world_id, soc_id, id = None):
        self.world_id = world_id
        self.soc_id = soc_id

        if not (id is None):
            self.load(id)
        else:
            self.id = -1
            self.new()

    # load from database
    def load(self, id):
        self.id = id
        # loading mind's spheres
        for row in CUR.execute("SELECT spheres.id FROM spheres WHERE mind_id = :id", { "id": id }):
            #  init spheres
            if row.type == constants.WORLD_TYPE:
                self.sphereWorld = Sphere(row.id)
            elif row.type == constants.SOCIUM_TYPE:
                self.sphereSocium = Sphere(row.id)
            elif row.type == constants.REFLECTION_TYPE:
                self.sphereReflection = Sphere(row.id)

    # create new
    def new(self):
        init_data = self.init_features()
        #  init spheres
        self.sphereWorld = Sphere(None, { 'time': constants.TIMER_START,
                                          'energy': constants.ENERGY_MAX,
                                          'feature': init_data['world'],
                                          'type': constants.WORLD_TYPE })
        self.sphereSocium = Sphere(None, { 'time': constants.TIMER_START,
                                          'energy': constants.ENERGY_MAX,
                                          'feature': init_data['socium'],
                                          'type': constants.SOCIUM_TYPE })
        self.sphereReflection = Sphere(None, { 'time': constants.TIMER_START,
                                          'energy': constants.ENERGY_MAX,
                                          'feature': init_data['reflection'],
                                          'type': constants.REFLECTION_TYPE })
    
    # init start features
    def init_features(self):
        return {
            'world': random.randint(constants.FEATURE_MIN, constants.FEATURE_MAX),
            'socium': random.randint(constants.FEATURE_MIN, constants.FEATURE_MAX),
            'reflection': random.randint(constants.FEATURE_MIN, constants.FEATURE_MAX)
        }

    # save the mind and it's spheres
    def save(self):
        # saving the mind data
        if self.mid > 0:
            CUR.execute("UPDATE minds SET world_in = :wid, socium_in = :sid WHERE id = :id",
                { "wid": self.world_id, "sid": self.soc_id, "id": self.id })
        else:
            CUR.execute("INSERT INTO minds (world_in, socium_in) VALUES (:wid, :sid)",
                { "wid": self.world_id, "sid": self.soc_id })
            self.id = CUR.lastrowid

        # saving spheres
        self.sphereWorld.save()
        self.sphereSocium.save()
        self.sphereReflection.save()

    def sphere_turn(self, sphere, internal_in, external_in):
        # check if feature livetime is over
        if sphere.time == (constants.TIMER_FINISH - 1):
            sphere.energy = constants.ENERGY_MAX
            sphere.time = 0
            sphere.feature = sphere.feature_default
        else:
            out = 0

            inside = internal_in + external_in

            # if inside is negative - compensate from energy, else - increase energy
            if inside < 0:
                sphere.energy = sphere.energy - 1
            elif sphere.feature_default > sphere.feature:
                sphere.feature = sphere.feature + 1
            else:
                sphere.energy = sphere.energy + 1
                out = 1
            
            # if energy is not enough for feeding feature - compensate again from energy
            if (sphere.energy < sphere.feature) and (sphere.energy != 0):
                sphere.energy = sphere.energy - 1

            # if we can't compensate - change feature and generate negative out
            if sphere.energy == 0:
                sphere.feature = sphere.feature - 1
                out = -1

            sphere.time = sphere.time + 1
            sphere.out = out

        sphere.save()
        return sphere

    # reflect external params on mind condition
    def turn(self, world, socium):
        # get mind output from the last turn with self.sphereReflection.out






