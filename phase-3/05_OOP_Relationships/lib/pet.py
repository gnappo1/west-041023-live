from .owner import *
from .pet_owners import *
class Pet:
    all = []

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        type(self).all.append(self)
    
    def pet_owners(self):
        return [pet_owner for pet_owner in Pet_Owners.all if pet_owner.pet == self]
    
    def owners(self):
        return {pet_owner.owner for pet_owner in self.pet_owners()}
