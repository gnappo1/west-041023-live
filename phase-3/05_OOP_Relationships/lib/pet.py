from .owner import *
from .pet_owners import *
class Pet:
    all = []

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        type(self).all.append(self)

    def owners(self):
        pass


