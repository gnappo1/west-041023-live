import datetime


class Pet_Owners:
    all = []

    def __init__(self, owner, pet):
        self.owner = owner
        self.pet = pet
        self.adoption_date = datetime.datetime.now()
        type(self).all.append(self)
