from .appointment import *


class Doctor:
    all = []

    def __init__(self, name, field):
        self.name = name
        self.field = field
        type(self).all.append(self)

    def appointments(self):
        pass

    def patients(self):
        pass
