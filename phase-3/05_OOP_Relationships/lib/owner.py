class Owner:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        type(self).all.append(self)
 
    def pet_owners(self):
        return [pet_owner for pet_owner in Pet_Owners.all if pet_owner.pet == self]
    
    def pets(self):
        return {pet_owner.pet for pet_owner in self.pet_owners()}



from .pet import *
from .pet_owners import *
