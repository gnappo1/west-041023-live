import datetime
from .owner import Owner 

class Pet_Owners:
    all = []

    def __init__(self, owner, pet):
        self.owner = owner # the instance of this class belongs to a owner
        self.pet = pet # the instance of this class belongs to a pet
        self.adoption_date = datetime.datetime.now()
        type(self).all.append(self)

    @property
    def owner(self):
        return self._owner
        
    @owner.setter
    def owner(self, owner):
        if isinstance(owner, Owner):
            self._owner = owner
        else:
            raise TypeError('Owner must be an instance of the Owner class!')