
from sphere import Sphere
import random

import constants
from ..connector import CUR

class Mind:

    def __init__(self, world_id, soc_id, id = None):

        self.id = -1
        self.world_id = world_id
        self.soc_id = soc_id

        if not (id is None):
            self.load(id)
        else:
            self.new()


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
        
    def init_features(self):
        return {
            'world': random.randint(constants.FEATURE_MIN, constants.FEATURE_MAX),
            'socium': random.randint(constants.FEATURE_MIN, constants.FEATURE_MAX),
            'reflection': random.randint(constants.FEATURE_MIN, constants.FEATURE_MAX)
        }

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





